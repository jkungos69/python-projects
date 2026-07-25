# Ticket Discount Calculation

A simple python application that calculation ticket prices or transit fares based

# User Input Data:

- The program prompt the user for their **age** (e.g , "20")

the program asks if the user is currently a **student** (`yes` or `no`)

2.) Logic Process (`calculate_discount` function):
**Age 0-12 (Child) ** 50% discoynt $\rightarrow ""Php150""

- **Age 13 – 19 or Student:** Discounted Rate $\rightarrow$ **$270**
  - **Age 60+ (Senior):** 20% Discount $\rightarrow$ **$240**
  - **Standard Adult (20–59):** Full Price $\rightarrow$ **$300**

---

## 💻 Corrected & Complete Python Code

```python
def calculate_discount(age, is_student=False):
    # 1. Child Discount (Age 0 to 12)
    if age <= 12:
        return 150

    # 2. Teenager (Age 13 to 19) OR Student
    elif (13 <= age <= 19) or is_student:
        return 270

    # 3. Senior Citizen (Age 60 and above)
    elif age >= 60:
        return 240

    # 4. Standard Adult (No discount)
    else:
        return 300


# --- USER INPUT SECTION ---

# Convert the age string input into an integer
user_age = int(input("Enter your age: "))

# Clean input by trimming whitespace (.strip()) and converting to lowercase (.lower())
student_input = input("Student? (yes/no): ").strip().lower()

# Evaluates to True if user types 'yes', otherwise False
is_student = (student_input == "yes")


# --- FUNCTION CALL & OUTPUT ---

final_price = calculate_discount(user_age, is_student)

print(f"\nYou need to pay: ${final_price}")
```
