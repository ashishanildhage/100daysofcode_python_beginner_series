# start=0
# def game():
#     def start():
#         start+=1 #this will show error since start is not defined inside the function
#         #global start
#         start=1 #global start makes start inside the function same as the one outside the function. 
#     start()
# game()
# print(start)
# game.start() #error -AttributeError: 'function' object has no attribute 'start'

# #instead of all this confusion, return the variable from the function and then store it into an object
# begin=game() #hence preserving the value of variable globally


# #Global constants 
# PI=3.14
# INSTAGRAM_ID="@ashtagmusic"
# URL="wwww.linkedin.com/in/ashishanildhage"

# def piii():
#     PI=4
#     return PI
# a=piii()
# print(a)
# # this means global constants can be modified/changed 
# # but writing variables in capitals only reminds us not to modify it.

#-----------------
#Number Guessing Game
import sub12_NumberGuessing_logo
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
theNumber=randint(1,100)
print(sub12_NumberGuessing_logo.logo)
while True:
    difficulty=input("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """).lower()
    if difficulty =="easy":
        difficulty=EASY_LEVEL_TURNS
        break
    elif difficulty =="hard": 
        difficulty=HARD_LEVEL_TURNS
        break
    else:
        print("Invalid Difficulty Input")
while True:
    guess=int(input(f"""You have {difficulty} attempts remaining to guess the number.
Make a guess: """))
    if guess==theNumber:
        print(f"You got it! The answer was {theNumber}")
        break
    elif guess<theNumber:
        print("Too Low.")
        difficulty-=1
    elif guess>theNumber:
        print("Too High.")
        difficulty-=1
    elif 1>guess>100:
        print("Enter number between 0 and 100")    

    if difficulty<=0:
        print("You've run out of guesses, you lose.")
        break  
    else:
        print("Guess again.")



