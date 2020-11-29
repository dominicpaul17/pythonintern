num1= [0,1,2,3,4,5]
for i in range(len(num1)):
    num1[i] = num1[i]+2
    print(num1)

num = '54321'
print(num)
for a in num:
    num = num[1: ]
    print(num)
n1 = 0
n2 = 1
count = 0
n = int(input("enter the number of terms:"))
print(n1)
print(n2)
while(count <= n):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n2)
    count +=1
num = int(input("enter a number:"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //=10
if num ==sum:
    print(num,"it is an armstrong number")
else:
    print(num,"is not an armstrong number")

num3 = 9
for i in range(0,10):
    e = num*i
    print(e)

num5 = int (input("enter a number"))
if (num5 > 0):
    print("the number is positive")
else :
    print("the number is negative")

days = int(input("enter the number of days"))
age = days/365
print(age)
import math
o = (math.pi)/4
print(math.sin(o))
print(math.cos(o))
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def prod(x,y)
    print(x*y)
def prod(x,y)
    print(x/y)

print ("choose a operation")
print ("1.Addition")
print("2.subtraction")
print("3.multplication")
print("4.division")


while True:
    choice = input("select a chose")
    if choice in('1','2','3','4'):
        number1= float(input("enter a number:"))
        number2 = float(input("enter a number"))
        if choice == '1':
            add(number1,number2)
        elif choice == '2':
            sub(number1,number2)
        elif choice == '3':
            prod(number1,number2)
        elif choice == '4':
            div(number1,number2)
        break
    else:
        print("enter a valid choice")




