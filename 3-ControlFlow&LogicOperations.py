# no=int(input("Enter the number : "))
# if no%2:
#     print("This is an odd number")
# else:
#     print("This is an even number")

# #BMI calculator 2.0
# weight=float(input("Enter weight : "))
# height=float(input("Enter height : "))
# bmi=int(weight/(height*height))
# conclusion=""
# if bmi<=18.5:
#     conclusion="underweight"
# elif bmi>18.5 and bmi<25:
#     conclusion="normal weight"
# elif bmi>25 & bmi<30:
#     conclusion="overweight"
# elif bmi>30 & bmi<35:
#     conclusion="obese"
# else:
#     conclusion="clinically obese"
# print(f"Your BMI is {bmi}, you are {conclusion}.")    

# #Leap Year
# year=int(input("Enter the year : "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap Year")
#         else:
#             print("Not a Leap Year")
#     else:    
#         print("Leap Year")
# else:
#     print("Not a Leap Year")

# #Pizza Cost Calculator
# print("Welcome to the Pizza Deliveries")
# size=input("Enter the Pizza Size - S,M or L? : ")
# pepperoni=input("Do you want Pepperoni - Y or N? : ")
# cheese=input("Do you want Cheese - Y or N? : ")    
# Bill=0

# if size=="S": 
#     bill=15
#     if pepperoni=="Y": bill+=2
# elif size=="M": 
#     bill=20
#     if pepperoni=="Y": bill+=3
# elif size=="L": 
#     bill=25
#     if pepperoni=="Y": bill+=3
    
# if cheese=="Y": 
#     bill+=1

# print(f"Your final bill is: ${bill}")


# #LOVE Calculator
# print("Welcome to the Love Calculator")
# name1=input("Enter your name : ").lower()
# name2=input("Enter their name : ").lower()
# name=name1+name2
# total1=name.count("t")+name.count("r")+name.count("u")+name.count("e")
# total2=name.count("l")+name.count("o")+name.count("v")+name.count("e")
# print(f"Your love score is {total1}{total2}%")