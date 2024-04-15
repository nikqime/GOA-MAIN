inputs = []
for w in range(5):
    user_input = int(input("Enter a number: "))
    inputs.append(user_input)
even = []
for num in inputs:
    if num % 2 == 0:
        even.append(num)
print("original list:", inputs)
print("Evens", even)
