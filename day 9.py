r = lambda x,y:x*y
print(r(12,15))
from functools import reduce
fib_series= lambda n:reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib_series(8))
alist=[1,2,3,4]
multiplied_list = [element*2 for element in alist]
print(multiplied_list)
mylist = [9,18,77,36,54,63,72]
final = list(filter(lambda x:(x%9 == 0),mylist))
print("numbers divisible by 9",final)
LIST1 =[10,22,33,55,34]
even_count=len(list(filter(lambda x:(x%2 ==0),LIST1)))
print("even numbers in the list:",even_count)
