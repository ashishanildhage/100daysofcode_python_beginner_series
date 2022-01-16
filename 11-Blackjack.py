import random 
import sub11_blackjack_logo
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
above_11_cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
def decider(playerhand,computerhand):
    while sum(computerhand)<17:
        if sum(computerhand)>=11:
            computerhand.append(random.choice(above_11_cards))
        else:
            computerhand.append(random.choice(cards))

    print(f"Your final hand: {playerhand}")
    print(f"Computer's final hand: {computerhand}")

    if sum(computerhand) > sum(playerhand):
        print("You Lose.")
    elif sum(computerhand) < sum(playerhand):
        print("You Win!")
    elif sum(computerhand) == sum(playerhand):
        print("Push! It's a Draw.")

print(sub11_blackjack_logo.logo)
playerhand=random.sample(cards,2)
print(f"Your cards: {playerhand}")
computerhand=random.sample(cards,2)
print(f"Computer's first Card: {computerhand[0]}")
while True:

    decision=input("Type 'y' to get another card, type 'n' to pass: ")
    if decision=="n":
            decider(playerhand,computerhand)
            break
        
    elif decision=="y":
        if sum(playerhand)>=11:
            playerhand.append(random.choice(above_11_cards))
        else:
            playerhand.append(random.choice(cards))
        if sum(playerhand)>=21:
            print(f"Your final hand: {playerhand}")
            print(f"Computer's final hand: {computerhand}")
            print("You Lose.")
            break

        if sum(computerhand)>=11:
            computerhand.append(random.choice(above_11_cards))
        else:
            computerhand.append(random.choice(cards))
        if sum(computerhand)>=21:
            print(f"Your final hand: {playerhand}")
            print(f"Computer's final hand: {computerhand}")
            print("You Win.")
            break

        print(f"Your cards: {playerhand}")
        print(f"Computer's first Card: {computerhand[0]}")
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

#Congratulations! Built the Blackjack Game WITHOUT ANY HINTS!!!

##################### The End #########################




