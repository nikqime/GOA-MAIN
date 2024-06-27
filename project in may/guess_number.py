import random
def numberguessinggame():
    number_to_guess = random.randint(1 , 100)
    pope = 0
    print("i am thinkng number between 1 and 100")
    while True:
        guess = input("say number: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        pope += 1
        if guess<number_to_guess:
            print("nah my number is bigger")
        elif guess > number_to_guess:
            print("my number is lower baby")
        else:
            print(f"браво босс, браво. за {pope} попиток")
            break
numberguessinggame()