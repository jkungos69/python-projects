name = "John"

greeting = "Welcome, " + name

greeting_length = len(greeting)

border = "=" * 25

print(border)
print(greeting)
print(f"Message Length: {greeting_length} characters")
print(border)

number = [1,2,4,5,6]

print(number[1:6])
print(number[::2])


cat = "Puti"

pet = "w" + cat[::2]

print(pet)


answer = " YES"

answer.strip()
answer.lstrip()
answer.rstrip()