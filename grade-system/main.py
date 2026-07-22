def get_remark(grade):
    if grade < 0 or grade > 100:
        return "Invalid Grade"
    elif grade >= 90:
        return "Excellent"
    elif grade >= 85:
        return "Very Good"
    elif grade >= 80:
        return "Good"
    elif grade >= 75:
        return "Passed"
    else:
        return "Failed"


name = input("Student Name: ")
grade = float(input("Enter Grade: "))

print("\n========== REPORT ==========")
print(f"Student : {name}")
print(f"Grade   : {grade}")
print(f"Remark  : {get_remark(grade)}")