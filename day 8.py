print("choose a operation:")
print("1.addtion")
print("2.subtraction")
print("3.multiplication")
print("4.division")

while True:
    choice =input("select a choice")

    if choice in('1','2','3','4'):
        num1 = int(input("enter a number:"))
        num2 = int(input("enter a number"))
        if choice == '1':
            print(num1+num2)
        elif choice == '2':
            print(num1-num2)
        elif choice == '3':
            print(num1*num2)
        elif choice == '4':
            try:
                num1/num2
            except ZeroDivisionError:
                print("division by zero is infinty")
        break
    else:
        print("enter a valid choice")

try:
    a = mangnoolia
except NameError:
    print("NO NAME IS DEFINED")
try:
    b =1/0
except ArithmeticError:
    print("Division by zero")
try:
    a = int(input("enter a value"))
    b = a/0
except ZeroDivisionError:
    print("not an error")


#try block is required for inbuilt functions whereas it is not required for any user defined execption