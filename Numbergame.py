# Python program for a random game about guessing the magic number

import random
print("The magic number is between 1 and 20")
guess = int(input("Your guess: "))
magic_number = random.choice(range(20))
if guess == magic_number:
    print("You guessed right!")
elif guess >= (magic_number - 5) and guess <= (magic_number + 5):
    guess = int(input("You're close! Try again "))
    if guess == magic_number:
        print("You did it!")
    else:
        print("Game over")
elif guess in range(20) and guess != magic_number:
    guess = int(input("Nope! Try again: "))
    if guess == magic_number:
        print("You won!")
    else:
        print("Game over")
else:
    print("Choose a number between 1 and 20")
    guess = int(input())
    if guess == magic_number:
        print("You guessed right!")
    else:
        print("Game over!")
print(f"The magic number is: {magic_number}")
