number1=int(input("Enter first number here : "))
number2=int(input("Enter second number here : "))
number3=int(input("Enter third number here : "))
number4=int(input("Enter fourth number here : "))
listt=[]

for i in range(1, number1+1):
    if number1 % i== 0:
        listt.append(i)
        

for u in range(1, number2 +1):
    if number2 % u ==0:
        listt.append(u)
       

for y in range (1 , number3 +1):
    if number3 % y == 0:
        listt.append(y)
        

for x in range (1 , number4 +1):
    if number4 % x ==0:
        listt.append(x)

listtt=sorted(listt)
print(listtt)