import os

secret_num = int(input("Player One, give me a number: "))

os.system('cls')

guess = int(input("Player Two, what's your guess? "))

if guess == secret_num:
    print("YOU WIN")
else:
    print("YOU LOSE.")
