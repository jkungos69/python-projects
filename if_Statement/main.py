"""

number = -2

def is_positive(number):
    if number > 0 :
        return True 
    else:
        return False 

print(is_positive(number))

"""


# Ticketing Discount

def calculate_discount(age, is_student = False):
    ticket_price = 300

    if age <= 12:
        return 150
    elif( 13 <= age <= 19) or is_student:
        return 260
    elif age >= 60:
     return 240
    else: 
        return " 300 No discount"

user_age = int(input("Enter your age: "))


student_input = input("Student? (yes/no): ").strip().lower()
is_student = (student_input == "yes")

final_price = calculate_discount(user_age, is_student)

print(f"\nYou need to pay : Php{final_price}")