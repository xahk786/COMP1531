import random

def guess_check(g, lower, upper):
    status = input("Is my guess too low (L), too high (H), or correct (C)?\n")

    if status == 'C' or status == 'c':
        print("Got it!")
        return
    
    if status == 'L' or status == 'l':
        lower = g
    elif status == 'H' or status == 'h':
        upper = g 

    new_guess = random.randint(lower,upper)
    print("My guess is:", + new_guess)
    return guess_check(new_guess, lower, upper)

if __name__ == "__main__":
    print("Pick a number between 1 and 100 (inclusive)")
    lower = 1
    upper = 100
    guess = random.randint(lower, upper)
    print("My guess is:", + guess)
    
    guess_check(guess, lower, upper)
