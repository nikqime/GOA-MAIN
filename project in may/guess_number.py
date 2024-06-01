import random

def numberguessinggame():
    number_to_guess = random.randint(1, 100)
    попиток_бля = 0
    
    print("hi")
    print("i am thinkng number between 1 and 100")
    
    while True:
        guess = input("say number: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        попиток_бля += 1
        
        if guess<number_to_guess:
            print("nah my number is bigger")
        elif guess > number_to_guess:
            print("my number is lower baby")
        else:
            print(f"браво босс, браво. за {попиток_бля} попиток")
            break

if __name__ == "__main__":
    numberguessinggame()