import random

number = random.randrange(1, 50)

chanceCount=0

class color:
    RED = '\033[91m'
    BOLD ='\033[1m'
    END ='\033[0m'

print("---------------------------------")
print(color.RED + color.BOLD + "Number guessing game" + color.END)
print("---------------------------------")
print("Guess a number (between 1 and 50)")
print("You have 5 chances.")
print("---------------------------------")

while chanceCount < 10:
    guess = int(input("Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < number:
        print("Too low! Guess a number higher than ", guess)
        print("---------------------------------")
        
    if guess > number:
        print("Too high! Guess a number lower than ", guess)
        print("---------------------------------")

    if guess == number:
        print("You win!!")
        break

    if not chanceCount < 10:
        print("You lose! The number is ", number)
