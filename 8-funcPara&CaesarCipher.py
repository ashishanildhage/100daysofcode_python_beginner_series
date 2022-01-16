def greet_with_name(name,location):
    print(f"""
    Hey There
    You are {name}
    from {location}""")

greet_with_name(location=input("Enter location"),name=input("Enter name"))

#--------------------------
#paint cans calculator
def paint_calc(height,width,cover):
    noOfCans=round((height*width)/cover)
    print(f"You'll need {noOfCans} cans to paint.")

h=int(input("Enter height of wall : "))
w=int(input("Enter width of wall : "))
c=5
paint_calc(height=h,width=w,cover=c)

#--------------------------
#Prime Number Checker - Not so good solution
def prime(no):
    count=0
    for i in range(2,101):
        if no%i==0:
            count+=1
    if count<=1:
        print("Its a prime number")
    else:
        print("Its not a prime number")

n=int(input("Check this number : "))
prime(n)


#Prime Number - Original good solution
def prime(no):
    check=False
    for i in range(2,no):
        if no%i==0:
            check=True
    if check:
        print("Its a prime number")
    else:
        print("Its not a prime number")
        
n=int(input("Check this number : "))
prime(n)

#--------------------------
#Caesar Cipher Shifting Encryption
import sub8_caesar_logo
def caesar(text,shift,crypt,alpha,number,symbols):
    newtext=""
    if crypt=="dec":  
        shift*=-1
    for i in text:
        if i not in number and symbols:
            newIndex=alpha.index(i)+shift
            newtext+=alpha[newIndex]
        else:
            newtext+=i
    print(newtext)

print(sub8_caesar_logo.logo)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","<",">","#","@","$","%","^"]
while exit:
    crypt = input("Type 'enc' to encrypt, type 'dec' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26
    exit=True
    caesar(text,shift,crypt,alpha,number,symbols) 
    wronginput=True
    while wronginput:
        exitter=input(" Do you want to continue? (y/n): ").lower()
        if exitter=="n":
            print("Goodbye")
            wronginput=False
            exit=False
        elif exitter=="y":
            wronginput=False
            pass
        else:
            print("Invalid answer")