# #HANGMAN - V1
# import random
# word_list=["ardvark","baboon","camel"]
# chosen_word=random.choice(word_list)
# guess=input("Guess a letter : ").lower()
# for i in chosen_word:
#     if guess==i:
#         print("Right")
#     else:
#         print("Wrong")

# #HANGMAN - V2
# import random
# word_list=["ardvark","baboon","camel"]
# chosen_word=random.choice(word_list)
# print(chosen_word+" is the answer.")
# fill=[]
# lives=0
# for _ in chosen_word:
#     fill.append("_")
# print(fill)
# while lives<len(chosen_word):
#     guess=input("Guess a letter : ").lower()
#     lives+=1
#     for i in chosen_word:
#         if guess==i:
#             fill.pop(chosen_word.index(i))
#             fill.insert(chosen_word.index(i),guess)
#     print(fill)
# if "_" in fill:
#     print("You Lost")
# else:
#     print("You Win")

# #hangman - v3 (Failed to do repeated words filing in the letters display)
# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# word_list=["ardvark","baboon","camel"]
# chosen_word=random.choice(word_list)
# print(chosen_word+" is the answer.")
# fill=[]
# for _ in chosen_word:
#     fill.append("_")
# print(fill)
# lives=6
# while lives>0:
#     print(stages[lives])
#     guess=input("Guess a letter : ").lower()
#     if guess not in chosen_word:
#         lives-=1
#     for i in chosen_word:
#         if guess==i:
#             fill.pop(chosen_word.index(guess))
#             fill.insert(chosen_word.index(guess),guess)
#     print(fill)
#     if "_" not in fill:
#         print("You Win")
#         break
# if lives==0:
#     print(stages[0])
#     print("You Lose")


#ORIGINAL HANGMAN - v4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])


#Final HANGMAN - v5
import random
import sub7_hangman_words
import sub7_hangman_logo
print(sub7_hangman_logo.logo)
end_of_game = False
chosen_word = random.choice(sub7_hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in display:
        print(f"You've already guess {guess}")   
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(sub7_hangman_logo.stages[lives])

