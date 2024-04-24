piper = 2400
rico_per_shoot = 240
rico = 2300
bull = 3400

user_input = input("Are you interested in Rico or Bull? ")
answer = input("Which brawler's damage are you interested in? Bull, Piper, or Rico (per attack): ")

if answer == "bull" or answer == "Bull":
    print("Bull's damage in near range: 3400. Are you interested in mid and long range?")
    user_input = input("Yes/No: ")
    if user_input == "Yes" or user_input == "yes":
        print("At mid range, damage = 1700. At long range, damage = 540.")

elif answer == "Piper" or answer == "piper":
    print("Piper's damage per attack:", piper)
    user_input = input("Are you interested in something else related to Piper's damage? Yes/No: ")
    if user_input == "Yes" or user_input == "yes":
        print("Additional information about Piper.")
    else:
        print("Okay, thank you.")

elif answer == "Rico" or answer == "rico":
    print("Rico's damage per attack:", rico_per_shoot)

else:
    print("Invalid input. Please choose Bull, Piper, or Rico.")
