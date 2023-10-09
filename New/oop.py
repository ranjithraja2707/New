class raja: #class
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print("the brand of the car is",self.brand)
d = raja("TaTa","Red") #object
print(d.brand)
print(d.color)
print(d.drive())
