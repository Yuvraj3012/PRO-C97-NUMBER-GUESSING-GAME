import random
print("Number guessing game")
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("Enter your guess: "))
    if guess==number:
        print("Congratulation you won")
        break
    elif guess<number:
        print("guess a higer number than",guess)
    else:
        print("guess a lower number than",guess)
    chances=chances+1
if not chances<5:
    print("You lose the number was ",number)                  