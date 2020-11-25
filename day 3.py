dict1 = {"apple":2 ,
         "orange":3,
         "banana" :4
         }
dict2 = {"cashew" : 2,
          "almond": 3
          }
dict1.update(dict2)
print ("merging two python dictionaries")
print(dict1)
print ("remove a key from dictionaries")
del dict1["apple"]
print(dict1)
keys = ['tata','maruti','audi']
values = ['altroz' , 'swift', 'q7']
print("map two list into a dictionary")
cars= dict(zip(keys,values))
print (cars)
dict5 = ('aaron','aakash','deepak','samuel','meera','gayathri')
print("find the length of the set")
print (len(dict5))
d1 = {1,2,3,4,5,6,7}
d2 = {1,2,6,7,8,9,}
print("the intersection of a 2nd set from the 1st set")
print(d1-d2)
