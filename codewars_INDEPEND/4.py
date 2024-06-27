# installed games
games = [
    'Soccer', 
    'Tic Tac Toe', 
    'Snake', 
    'Puzzle', 
    'Rally'
]

choice = int(input("Enter the game number (0-4): "))

if 0 <= choice < len(games):
    print(games[choice])
else:
    print("Invalid choice. Please enter a number between 0 and 4.")