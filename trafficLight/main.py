def traffic_light_control(light_color, is_emergency = False):
    if is_emergency:
        return "GO! Priority and Emergency Vehicle!"
    elif light_color == "1":
        return "Stop"
    elif light_color == "2":
        return "Slow Down"
    elif light_color == "3":
        return "GO"
    else:
        return "Invalid Choice! (Please select 1, 2, or 3)"


print("=== SMART TRAFFIC LIGHT SYSTEM ===")
print("Select the traffic light color:")
print("[1] Red")
print("[2] Yellow")
print("[3] Green")

color_choice = input("Enter your choice (1-3): ").strip()

emergency_input = input("Is there an emergency Vehicle? (yes/no)").strip(). lower()
is_emergency = (emergency_input == "yes")

result = traffic_light_control(color_choice, is_emergency)

print("\nResult", result)