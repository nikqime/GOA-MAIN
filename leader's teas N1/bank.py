balance=0
def create_account():#ფუნქცია შევქმენი
    question1=input("do u have bank account? yes/no: ")#ბასე კითხვა
    if question1=="yes":
        usernamee=input("Enter your username here: ")#შესვლა ეცაუნთში
        passwordd=input("Enter your password here: ")
        print("u succesfully log in, now what u want do?")#შემდეგ ეტაპზე გადასვლისთვის ვეკითხები რაუნდა ამ ექვსიდან
        choose()
    elif question1=="no":#იმ შემთხვევაში თუ არ აქვს ბანკის ეცაუნთი
        account_createing="So for what are u waiting for? Create account. u want to make account? yes/no : "#ვეკითხები უნდა თუ არა შექმნა
        print(account_createing)
        if account_createing=="yes":
            print("NICE. now choose your username end create password")
            username=input("Enter your username here: ")
            password=input("Enter your password here: ")
            repet_password=input("repet your password")
            if password!=repet_password:#თუ პაროლი არასწორია ხელმეორედ log in
                print("your passord repet was not correct so log in again")
                username=input("Enter your username here: ")
                password=input("Enter your password here: ")
                repet_password=input("repet your password: ")
                if password==repet_password:
                      choose()
        elif account_createing=="no":
            print("ok i am SAD now")
    else:
        False
create_account()
def choose():
    print('''        1.make_transaction
        2.withdraw
        3.delete_account
        4.account_info
        5.delete account
        6.exit system
            ''')
    print("1-6")

    question2=input("Enter number 1-6 for turning function u want : ")#აქ ვნომრავ ექვსივე ფუნქციას რომ მომხმარებელმა შეძლოს არჩევა და შემდეგ მაგ ფუნქციაზე გადასვლა
    if int(question2)<=6 and int(question2)>=1:
        if question2==1:
            make_transaction()
        elif question2==2:
            withdraw()
        elif question2==3:
            delete_account()
        elif question2==4:
            account_info()
        elif question2==5:
            delete_account()
        elif question2==6:
            exit_system()

def deposit():
    balance=0
    print("how much u want to deposit")#რამდენი უნდა რომ შეიტანოს
    depo1=input("Enter amount here: ")#რაოდენობა თუ რამდენი უნდა
    if depo1>=1:
        balance+=depo1#აქ უბრალოდ რომ დაემატოს ბალასს იმდენი რამდენისაც დაადეპოზიტებს
def make_transaction():
    question_transaction1="hello to who u will tranact money? to your self or to someone? youself/someone"#ტრანზაქციის შეკითხვა
    print(question_transaction1)
    if question_transaction1=="yourself":
        print("ok")
        self_angarishze_tranzaqcia=input("Enter how much u will transite to your account and enter phone number or your account")#ვის და რამდენს გადაურიცხავს
        if self_angarishze_tranzaqcia>balance:
            question_transaction2="u can not afford transaction. do u want to deposit? yes/no"#ბალანსი თუ საკმარისი არ არის მაშინ დეპოზიტი უნდა თუ არა ეკითხება
            print(question_transaction2)
            if question_transaction2=="yes":
                deposit()
            elif question_transaction2=="no":
                False
        elif self_angarishze_tranzaqcia<balance:
            transaction2="Enter amount how much u will transact here: "
            print(transaction2)
            

def withdraw():

    print("I will remaind u that you balance is")
    print(f"{balance}")
    print(f"so u can max withdraw {balance}$ ")
    question1_withdraw=input("Enter amout that u want to withdraw here: ")
    if question1_withdraw>balance:
        False
    elif question1_withdraw<=balance:
        print(f"u withdrawed succsesfully {question1_withdraw} and your balance is now {balance-question1_withdraw}")

def delete_account():

    print("it will be ready soon")

def account_info():

    print("in account info we don't have many INFO about u at the momnet we can say only your balance.")
    print("MORE WILL BE SOON")
    print(f"{balance}")#აქ f"ს მეშვეობით ვეუბნები ბალანსს რაც იმ მომენტში აქვს როდესაც იკითხავს

def delete_account():

    print("it will be ready soon")

def exit_system():

    print("it will be ready soon")








