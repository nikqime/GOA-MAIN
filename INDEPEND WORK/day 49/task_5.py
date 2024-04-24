number = int(input("შემოიტანეთ რიცხვი: "))

if number > 1 :                                             
    for i in range(2, number):                                   
        if number % i == 0:
            print("თქვენი რიცხვი არ არის მარტივი")                                        
            break
    else:
        print("თქვენი რიცხვი მარტივია")