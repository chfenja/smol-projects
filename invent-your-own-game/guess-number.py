import random

guessesTaken = 0

myName = input("Hello! What's your name? ")

number = random.randint(1, 20)
print(f"Well, {myName.title()}, I'm thinking of a number between 1 and 20.")

for guessesTaken in range(6):
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Your guess is too low.")

    elif guess > number:
        print("Your guess is too high.")

    elif guess == number:
        print(f"Good job, {myName.title()}!"
              f"You guessed my number in {guessesTaken} guesses!")
        break

if guess != number:
    print(f"Nope. The number I was thinking of was {number}.")
