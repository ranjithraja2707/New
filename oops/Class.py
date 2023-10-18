class parent_class():
    def parent_method(self):
        print("This is in parent class") #parent class

class child_class(parent_class):    #child class
    def child_method(self):
        print("This is in child class")
obj = child_class()
obj.parent_method()
obj.child_method()