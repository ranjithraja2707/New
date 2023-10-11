# Python code for accessing methods using static method
class test:
	@staticmethod #it does receive the implicit as First Parameter instead of self.
	def square(x):
		test.result = x*x

t1=test()
t2 = test()
t1.square(5)
print (t1.result)
t2.square(10)
print (t2.result)
print (t1.result)
