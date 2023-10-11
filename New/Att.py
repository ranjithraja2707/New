# Python code for accessing attributes of class
class emp:
	name='Ranjith'
	salary='10,000'
	def show(self):
		print (self.name)
		print (self.salary)
e1 = emp()
print (getattr(e1,'name')) # Use getattr instead of e1.name
print (hasattr(e1,'name')) # returns true if object has attribute
setattr(e1,'height',152) # sets an attribute
print (getattr(e1,'height')) # returns the value of attribute name height
delattr(emp,'salary') # delete the attribute

