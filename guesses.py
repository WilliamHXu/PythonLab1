import random

def guessing_game():
    print("Let's play a Game!")
    print("Guess a Number Between 1 and 100")
    answer = random.randint(1, 101)
    flag = False
    while not flag:
        guess = int(input("Please Make a Guess"))
        if answer == guess:
            flag = True
        elif guess > answer:
            print("Too High!")
        else:
            print("Too Low!")
    print("You Got It!")


guessing_game()
