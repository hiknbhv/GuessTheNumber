import random

random_num = random.randint(1,10)


while True:
    guess = int(input("What is your Guess? "))

    if guess > random_num:
        print("Too High, Try again")

    elif guess < random_num:
        print("Too Low, Try again")

    else:
        print("You Got It, YOU WIN")
        break
