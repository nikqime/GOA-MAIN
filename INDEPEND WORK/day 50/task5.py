kills=input("how many kills u made this round? : ")
headshots=input("how many headshots u made this round? :")
nonheadshots=input("how many default kills u made this round? :")

balance=100

balance=(int(headshots) * 600)+ (int(nonheadshots) * 300)
    
print(balance)

