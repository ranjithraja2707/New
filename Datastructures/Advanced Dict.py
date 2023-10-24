a = ['a',3,4,5,7]
b = {i:i for i in a}
print(b)
print("//Sorting in dict//")
d = {'b':3,'c':1,'a':2}
f = sorted(d) #sorting based on its keys
print(f)
f = sorted(d, key=lambda x: d[x]) #here I mentioned keys and values .
print(f)    #Sorting based on its values.
print("//Merging Dictionaries//")
b.update(d)
print(b)
print("//Using **b,**a to merge two dict")
m = {**b,**d}
print(m)
