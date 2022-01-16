#Heads or Tails
import random
a=random.randrange(0,2)
Toss="Heads" if a==1 else "Tails"

#Who will pay the bill?
import random
people=input("Enter people seperated by , : ")
peoples_list=people.split(',')
print(peoples_list)
random_choice=random.randint(0,len(peoples_list)-1)
print(peoples_list[random_choice]+" will pay the bill.")

#Tresure matrix
import random
matrix=[["","",""],["","",""],["","",""]]
place=input("Where do you want to put the treasure? Enter column and row without space")
matrix[int(place[1])-1][int(place[0])-1]="*"
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

#Rock, Paper & Scissors - Human vs CPU
import random
human=int(input("Enter 0,1 or 2 for Rock, Paper & Scissors"))
cpu=random.randrange(3)
print(human,cpu)
if human==cpu:
    print("Its a Draw")
elif human==2 and cpu==0:
    print("You Lose")
elif human>cpu:
    print("You Win")
else: 
    print("You Lose")   