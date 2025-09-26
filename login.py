import guess
def login():
    while True:
        pwsd=int(input("enter the password= "))
        if pwsd==2005:
            print("in process!!please wait")
            guess.game()
        else:
            print("invalid !try again")

if __name__=="__main__":
    print("welcome")
    login()


    