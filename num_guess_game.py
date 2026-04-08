import random

number = random.randint(1, 10)
attempt = 0

while True:
    guess = int(input("Enter your guess (1 to 10) : "))
    attempt += 1

    if (guess > number):
        print("Too High")
    elif (guess < number):
        print("Too Low")
    else:
        print("Correct guess")   
        print("Total Attempts", attempt)
        break
             
