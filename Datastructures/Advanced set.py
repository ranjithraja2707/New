a = {1,2,3,4,5}
b = {9,8,7,1,2}
c = a.union(b)
print(c)
c = a.intersection(b)
print(c)
c = a.difference(b)
print(c)
c = a.symmetric_difference(b)
print(c)
print("\u0332".join("Set Comprehension:"))
a = 10
d = {x+a for x in range(5) if x == 0}
print(d)
