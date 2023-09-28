def Recur_facto(n):

	if (n == 0):
		return 1

	return n * Recur_facto(n-1)

print(Recur_facto(6))

#fibbonacci series

def fun(n):
	if n <= 1: #base case
		return n
	else:
		return (fun(n-1) + fun(n-2)) #recursive case
n = 6
for i in range(6):
	print(fun(i))