from random import randint
import os
import sub14_HigherLowerGame_logo
import sub14_HigherLowerGame_gameData
score=0 
def end_game(score):
    """Ends the game by displaying the final score"""
    screen_clear()
    print(sub14_HigherLowerGame_logo.logo)
    print(f"Sorry that's wrong. Final Score : {score}")

def screen_clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

while True: 
    print(sub14_HigherLowerGame_logo.logo)

    if score==0:
        chosen_index_A=randint(0,49)
        chosen_data_A=sub14_HigherLowerGame_gameData.data[chosen_index_A]
    else:
        chosen_data_A=chosen_data_B
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {chosen_data_A['name']}, a {chosen_data_A['description']}, from {chosen_data_A['country']}")

    print(sub14_HigherLowerGame_logo.vs)

    #Different Random Index check
    while True:
        chosen_index_B=randint(0,49)
        if chosen_index_B!=chosen_index_A:
            break

    chosen_data_B=sub14_HigherLowerGame_gameData.data[chosen_index_B]
    print(f"Against B: {chosen_data_B['name']}, a {chosen_data_B['description']}, from {chosen_data_B['country']}")

    # More followers? - A or B
    while True:
        selection=input("Who has more followers? Type 'A' or 'B': ").upper()
        if selection == 'A' or selection == 'B':
            break
        else:
            print("Invalid Choice")
    if selection=='A':
        if chosen_data_A['follower_count']>chosen_data_B['follower_count']:
            score+=1
        else:
            end_game(score)
            break
    if selection=='B':
        if chosen_data_B['follower_count']>chosen_data_A['follower_count']:
            score+=1
        else:
            end_game(score)
            break

    screen_clear()

    
