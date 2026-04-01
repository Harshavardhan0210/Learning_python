import random

number = random.randint(1,100)
attempts = 0

print("Guess the number between 1 to 100")

while True:
    guess=int(input("Enter your Guess :"))
    attempts += 1

    if guess > number :
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct !!")
        print("No of Attempts :",attempts)
        break

