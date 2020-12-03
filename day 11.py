l1 = [1, 2, 3, 4]
l2 = [0, 8, 7, 9, 6]
ziplist = list(zip(l1, l2))
tuplelist = tuple(ziplist)
print(tuplelist)
import random

l3 = []
l4 = []
for i in range(1, 8):
    a = random.randint(1, 8)
    b = random.randint(1, 8)
    l3.append(a)
    l4.append(b)
ziplist1 = zip(l3, l4)
tuplelist1 = tuple(ziplist)
print(tuplelist1)
import random

l5 = []
for i in range(1, 10):
    x = random.randint(1, 30)
    l5.append(x)
sortedlist = sorted(l5)
print("the sorted list is ", sortedlist)
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def filteroddnum(num):
    if (num % 2) == 0:
        return true
    else:
        return false


filtered_number = filter(filteroddnum, l)
print("the filtered numbers are :",list(filtered_number))
