first = int(input("Enter first number here: "))
second = int(input("Enter second number here: "))
third = int(input("Enter third number here: "))
fourth = int(input("Enter fourth number here: "))
five = int(input("Enter fifth number here: "))

lst = []

if first > second and first > third and first > fourth and first > five:
    for i in range(0, first + 1):
        lst.append(i)
    print(lst)
