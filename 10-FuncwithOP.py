def capitalize(first,last):
    # return first.upper()[0]+first.lower()[1:]+" "+last.upper()[0]+last.lower()[1:]
    if first!="" or last!="":
        firstnew=first.title()
        lastnew=last.title()
        return f"{firstnew} {lastnew}"
    else:
        return "Invalid Inputs"

f_name=input("enter first name : ") 
l_name=input("enter last name : ") 
titlecase=capitalize(f_name,l_name)
print(titlecase)

#------------------------
#Leap Year
def is_leap(year):
    leap=True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                pass
            else:
                leap=False
        else:
            pass
    else:
        leap=False
    return leap

def days_in_month(year,month):
    """Returns the no. of days in the specific month considering if it is leap year or not.""" 
    #This is called Docstrings, Very useful for describing function,
    #while building a functions file for projects.
    if 12<month<1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year):
        month_days[1]=29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


#-------------------
#Calculator
import sub10_FuncwithOP_logo
print(sub10_FuncwithOP_logo.logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2    
def div(n1,n2):
    return n1/n2

n1=eval(input("Enter the First number : "))
exitter=True
while exitter:
    oper=input("+\n-\n*\n/\nSelect Operation : ")
    n2=eval(input("Enter the next number : "))
    operations={
        "+":add(n1,n2),
        "-":sub(n1,n2),
        "*":mul(n1,n2),
        "/":div(n1,n2)
    }
    answer=operations[oper]
    print(f"{n1} {oper} {n2} = {answer}")
    continuer=input("Type 'y' to continue calculations or 'n' to exit : ")
    if continuer=="n":
        exitter=False
        print("GoodBye!")
    elif continuer=="y":
        n1=answer