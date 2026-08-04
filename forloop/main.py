friends = ["John", "Raul", "Pat"]

for friend in friends :
    print("Hi " + friend)


fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")





def filter_long_words(word_list):

    filter_words = []

    for word in word_list:
        if len(word) > 4:
            filter_words.append(word)
    
    return filter_words


#Test Data

input_words = ["apple","cat","banana","dog","elephant"]

output = filter_long_words(input_words)
print(output)


def calculate_sum_and_average(numbers):

    if not numbers:
        return(0, 0.0)
    total = 0

    for num in numbers:
        total += float(num)
    
    average = total/len(numbers)
    return (total, average)




case_1 = [10, 20, 30, 40, 50]
print("Test 1: ",calculate_sum_and_average(case_1))

case_2 = [-5, 5, -10, 10]
print("Test 2 (Negatives):", calculate_sum_and_average(case_2))

case_3 = [42]
print("Test 3 (Single Item):", calculate_sum_and_average(case_3))

case_4 = [1.5, 2.5, 3.5]
print("Test 4 (Floats):", calculate_sum_and_average(case_4))

case_5 = []
print("Test 5 (Empty List):", calculate_sum_and_average(case_5))

string_nums = ["10", "20.5", "30"]
print("Resulta:", calculate_sum_and_average(string_nums))


for n in range(0,11,2):
    print(n)


def get_odd_numbers(start, end):

    odds = []

    for num in range(start, end + 1):
        if num % 2 != 0 :
            odds.append(num)
    return odds


print(get_odd_numbers(1, 10))  # Output: [1, 3, 5, 7, 9]

def countdown(start):
    for i in range(start, 1, 6):
        print(i)

    print("Boom")

countdown(6)


def print_multiplication_table(number):
    for i in range(0, 6):

        print(f"{number} x {i} = {number * i}")

print_multiplication_table(7)