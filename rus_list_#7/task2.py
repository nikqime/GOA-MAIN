sigrdze=int(input("enter lenght:"))
zero=0
list=[]

while zero<sigrdze:
    text="Enter the number" + str(zero+1) +":"
    list.append(input(text))
    zero+=1
print(list)