while True:
    print("\n--- MAIN MENU ---")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print("Your balance is: $1,000")
    elif choice == "2":
        print("Deposit successful!")
    elif choice == "3":
        print("Goodbye! Thank you for using.")
        break  # Breaks out of the loop to end the program
    else:
        print("Invalid choice, please select only from 1 to 3.")