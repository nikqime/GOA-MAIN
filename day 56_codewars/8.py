num1 = int(input("Enter #1 number here: "))
num2 = int(input("Enter #2 number here: "))
num3 = int(input("Enter #3 number here: "))
num4 = int(input("Enter #4 number here: "))
num5 = int(input("Enter #5 number here: "))

lst = []

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    lst.extend([num2, num3, num4, num5])

if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    lst.extend([num1, num3, num4, num5])

if num3 < num2 and num3 < num1 and num3 < num4 and num3 < num5:
    lst.extend([num2, num1, num4, num5])

if num4 < num2 and num4 < num3 and num4 < num1 and num4 < num5:
    lst.extend([num2, num3, num1, num5])

if num5 < num2 and num5 < num3 and num5 < num4 and num5 < num1:
    lst.extend([num2, num3, num4, num1])

print(lst)