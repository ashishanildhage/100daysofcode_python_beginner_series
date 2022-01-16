#find average of students heights
import random
heights=[]
avg=0
max=0
n=int(input("Enter number of Students"))
for _ in range(n):
    i=int(input())
    avg+=i
    if i>max:
        max=i
    heights.append(i)
print(abs(int(avg/n)))
print(max)

#Print even numbers from 1 to 100 and add them up
sum=0
for n in range(2,101,2):
    sum+=n
    print(n)
print(sum)

#FizzBuzz Challenge
for i in range(0,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else: print(i)

#Password Generator
import random
letters="pqwoeirutylaskdjfhgmzxnbcv"
symbols="~!@#$%^&*()_+`;-=[]:\"\'<>?,./|\\\'"
numbers="0123456789"
l=int(input("Enter number of letters : "))
s=int(input("Enter number of symbols : "))
n=int(input("Enter number of numbers : "))
new,password="",""
for i in range(l):
    new+=random.choice(letters)
for j in range(s):
    new+=random.choice(symbols)
for k in range(n):
    new+=random.choice(numbers)
passlist=[]
for x in new:
    passlist.append(x)
random.shuffle(passlist)
for y in passlist:
    password+=y
print(password)

