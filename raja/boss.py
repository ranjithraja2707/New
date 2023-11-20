a = [[1],[2]]
x = " ".join(list(map(str,a)))
print(x)
x = str(5)
print(type(x))

a = [1,2,3,4,5]
for i in range(1,5):
    a[i-1] = a[i]
    for i in range(0,5):
        print("raja")
print(a[i],end=" ")

a = 165
b = sum(list(map(int,str(a))))
print("\n",b)