lst = []
for i in range(15):
    item = int(input("please input an item: "))
    lst.append(item)

odd = []
even = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"the list that you wrote is {lst}")
print(f"the odd numbers from this list are {odd}")
print(f"the even numbers from this list are {even}")