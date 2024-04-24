def gamravleba(x, y):
    lst = []
    for i in range(1, y + 1):
        lst.append(x * i)
    return lst
x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))
result = gamravleba(x, y)
print("The first", y, "multiples of", x, "are:", result)