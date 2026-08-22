user_email = "kevin.ungos@gmail.com"

clean_email = user_email.strip().lower()

if "@" in clean_email:
    at_index = clean_email.index("@")
    username = clean_email[:at_index]
    domain = clean_email[at_index + 1:]

    print(f"UserName: {username}")
    print(f"Domain: {domain}")

else:
    print("Invalid Email: Walang '@' symbol!")
