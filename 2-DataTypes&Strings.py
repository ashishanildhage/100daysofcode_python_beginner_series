inp=input()
out=int(inp[0])+int(inp[1])
print(f"{inp[0]} + {inp[1]} = {out}")
print(out)

#BMI calculator
weight=float(input("Enter weight : "))
height=float(input("Enter height : "))
bmi=int(weight/(height*height))
print(bmi)

#Life left until 90 years
age=int(input("Enter age : "))
years_left=90-age
months_left=years_left*12
weeks_left=years_left*52
days_left=years_left*365
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")

#Bill calculator
print("Welcome to the Tip Calculator")
total=float(input("What was the Total Bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10,12 or 15? "))
tip=total*(tip_percentage/100)
total_with_tip=total+tip
count=int(input("How many people to split the bill? "))
per_bill=round(total_with_tip/count,2)
print(f"Each person should pay: ${per_bill}")