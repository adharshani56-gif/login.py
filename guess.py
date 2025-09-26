import random
def game():
    secret=random.randint(1,10)
    for i in range(1,4):
        guess=int(input("enter your guess"))
        if guess==secret:
            print("YOU SUCCEED")
            break
        elif guess>secret:
            print("your guess is too high")
        elif guess<secret:
            print("Your guess is too low")
        else:
            print("your guess is not between my secret")
