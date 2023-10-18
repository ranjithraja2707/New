class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass
    def display_color(self):
        print(f"The shape is {self.color} in color.")
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
circle.display_color()
print("Circle Area:", circle.area())
rectangle.display_color()
print("Rectangle Area:", rectangle.area())
