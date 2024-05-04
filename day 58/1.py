listt = input("Enter numbers: ")
lst = listt.split()

min_number = min(map(int, lst))
lst.remove(str(min_number))

print(lst)