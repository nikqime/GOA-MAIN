def creating(GOA, account):
    if account == "yes":
        print("Okay, account created at GOA bank.")
    elif account == "no":
        print("Alright, no account created.")
    else:
        print("Invalid input.")

account = input("Do you want to make your account in GOA bank? (yes/no): ")
creating("GOA Bank", account)

question1 = input("What do you want to do? -- invest, withdraw, or take a loan: ")

if question1 == "invest":
    def inv(invest, balance):
        amount = float(input("How much do you want to invest? "))
        balance += amount
        print(f"Now you added {amount} dollars to your balance.")
        print(f"Your balance now is {balance} dollars.")
    
    balance = 0  # Starting balance
    inv(question1, balance)



       








