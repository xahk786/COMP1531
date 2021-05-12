import random

print("Pick a number between 1 and 100 (inclusive)")

y = 1
z = 100
guess = random.randint(1, 100)

new_list = []

while (True):
    print("My guess is:", + guess)
    x = input ('Is my guess too low (L), too high (H), or correct (C)?\n')
    if x == "L":
        y = int(guess)
        guess = random.randint(y, z)
        while True:
            if int(guess) in new_list:
                guess = random.randint(y, z)
            else:
                break
    elif x == "H":
        z = int(guess)
        guess = random.randint(y, z)
        while True:
            if int(guess) in new_list:
                guess = random.randint(y, z)
            else:
                break

    elif x == "C":
        print("Got it!")
        break
    new_list.append(guess)
        











