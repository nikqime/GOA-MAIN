listt = []
listtt = []

a = int(input("Enter first number here: "))
b = int(input("Enter second number here: "))

if a > b:
    for i in range(b, a):
        listt.append(i)
    print(listt)
        
elif b > a:
    for j in range(a, b):
        listtt.append(j)
    print(listtt)