class MyClass: #class
  x = 5
print(MyClass)

class MyClass: # class
  y = 5
  x = 10
p1 = MyClass() #object
print(p1.y)
print(p1.x)

class raja:
  def __init__(self,x,y): #using __init__ and also using function(Method) within the class. 
    self.z = x + y
my_object = raja(5,10)
print(my_object.z)