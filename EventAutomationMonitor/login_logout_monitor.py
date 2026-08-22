import argparse
import csv
import json
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


EVENTS = {
    "4624": "login",
    "4634": "logout",
    "4647": "user_logout",
    "4800": "lock",
    "4801": "unlock",
}

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CSV = BASE_DIR / "events.csv"
DEFAULT_STATE = BASE_DIR / "monitor_state.json"


def run_wevtutil(max_events):
    event_ids = " or ".join(f"EventID={event_id}" for event_id in EVENTS)
    query = f"*[System[({event_ids})]]"
    command = [
        "wevtutil",
        "qe",
        "Security",
        f"/q:{query}",
        "/f:xml",
        f"/c:{max_events}",
        "/rd:true",
    ]

    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(message or "Could not read the Windows Security event log.")

    return completed.stdout


def parse_events(xml_text):
    if not xml_text.strip():
        return []

    root = ET.fromstring(xml_text)
    namespace = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
    rows = []

    for event in root.findall("e:Event", namespace):
        system = event.find("e:System", namespace)
        if system is None:
            continue

        event_id_node = system.find("e:EventID", namespace)
        record_id_node = system.find("e:EventRecordID", namespace)
        time_node = system.find("e:TimeCreated", namespace)
        computer_node = system.find("e:Computer", namespace)

        if event_id_node is None or record_id_node is None:
            continue

        event_id = event_id_node.text or ""
        record_id = int(record_id_node.text or "0")
        event_data = extract_event_data(event, namespace)
        timestamp = ""

        if time_node is not None:
            timestamp = time_node.attrib.get("SystemTime", "")

        rows.append(
            {
                "record_id": record_id,
                "timestamp_utc": timestamp,
                "timestamp_local": to_local_time(timestamp),
                "event_id": event_id,
                "event_type": EVENTS.get(event_id, "unknown"),
                "user": event_data.get("TargetUserName") or event_data.get("SubjectUserName") or "",
                "domain": event_data.get("TargetDomainName") or event_data.get("SubjectDomainName") or "",
                "logon_type": event_data.get("LogonType", ""),
                "computer": computer_node.text if computer_node is not None else "",
            }
        )

    return sorted(rows, key=lambda row: row["record_id"])


def extract_event_data(event, namespace):
    data = {}
    event_data = event.find("e:EventData", namespace)
    if event_data is None:
        return data

    for item in event_data.findall("e:Data", namespace):
        name = item.attrib.get("Name")
        if name:
            data[name] = item.text or ""
    return data


def to_local_time(timestamp):
    if not timestamp:
        return ""
    normalized = timestamp.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized).astimezone().isoformat(timespec="seconds")
    except ValueError:
        return ""


def load_last_record_id(state_path):
    if not state_path.exists():
        return 0
    try:
        return int(json.loads(state_path.read_text(encoding="utf-8")).get("last_record_id", 0))
    except (OSError, ValueError, json.JSONDecodeError):
        return 0


def save_last_record_id(state_path, record_id):
    state_path.write_text(
        json.dumps({"last_record_id": record_id, "updated_utc": datetime.now(timezone.utc).isoformat()}),
        encoding="utf-8",
    )


def append_events(csv_path, rows):
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not csv_path.exists()

    with csv_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "record_id",
                "timestamp_utc",
                "timestamp_local",
                "event_id",
                "event_type",
                "user",
                "domain",
                "logon_type",
                "computer",
            ],
        )
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


def collect_new_events(csv_path, state_path, max_events):
    last_record_id = load_last_record_id(state_path)
    rows = [
        row
        for row in parse_events(run_wevtutil(max_events))
        if row["record_id"] > last_record_id
    ]

    if rows:
        append_events(csv_path, rows)
        save_last_record_id(state_path, rows[-1]["record_id"])

    return rows


def main():
    parser = argparse.ArgumentParser(description="Monitor Windows login/logout events with Python.")
    parser.add_argument("--once", action="store_true", help="Collect new events once, then exit.")
    parser.add_argument("--interval", type=int, default=10, help="Seconds between checks.")
    parser.add_argument("--max-events", type=int, default=50, help="Number of recent Event Log records to query.")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="CSV output path.")
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE, help="State file path.")
    args = parser.parse_args()

    while True:
        try:
            rows = collect_new_events(args.csv, args.state, args.max_events)
            for row in rows:
                print(
                    f"{row['timestamp_local']} {row['event_type']} "
                    f"{row['domain']}\\{row['user']} record={row['record_id']}"
                )
        except RuntimeError as error:
            print(f"Error: {error}", file=sys.stderr)
            print("Tip: run PowerShell as Administrator if Security log access is denied.", file=sys.stderr)
            return 1

        if args.once:
            return 0

        time.sleep(max(args.interval, 1))


if __name__ == "__main__":
    raise SystemExit(main())

