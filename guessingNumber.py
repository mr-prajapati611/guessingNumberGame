import random

num = random.randint(1, 100)

tries = 0

while True:
    guess = int(input("Please guess your number b/w 1 and 100: "))
    tries += 1

    if num == guess:
        print(f"you're right, you've guessed the number in {tries} tries")
        break
    elif num > guess:
        print("go a little higher")
    elif num < guess:
        print("go a little lower")