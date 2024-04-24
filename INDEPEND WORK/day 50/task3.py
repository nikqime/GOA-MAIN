num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))

numbers = []

# Finding factors of num1
for num in range(1, num1 + 1):
    if num1 % num == 0:
        numbers.append(num)

# Finding factors of num2
for num_2 in range(1, num2 + 1):
    if num2 % num_2 == 0:
        numbers.append(num_2)

print("Factors of", num1, "and", num2, "are:", numbers)