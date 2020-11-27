def arith_op(x,y):
    print("add",x+y)
    print("sub",x-y)
    print("multi",x*y)
    print("div",x/y)
a = input("enter a value")
b = input("enter a value")
c= int(a)
d = int(b)
print(arith_op(c,d))

def covid(patient_name,body_temp = "98f"):
    print(patient_name)
    print(body_temp)
    print("the body temperature of "+patient_name +"body_temp")
e = input ("enter the name:")
covid(e)