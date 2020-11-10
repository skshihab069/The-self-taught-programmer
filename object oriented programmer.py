# class is a constructor or a blueprint for a object
# every object has some kind of attribute and methods
# class has 2 types of variable 1.class variables 2.Instance variables
# we use the _init_(self) function to assign  values to object properties
# _init_ function is automatically called every time and object is created
# the variables of objects are called properties
# the functions of objects are called methods
# the (self)  parameter is  used to access the variables that belong to objects
# You can inherit all the functionalities of a class by

class Shapes:
    def who_i_am(self):
        return print("I am a shape")


class Rectangle(Shapes):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimiter(self):
        return self.width * 2 + self.length * 2


class Square(Shapes):
    def __init__(self, surface):
        self.surface = surface

    def calculate_area(self):
        return self.surface * self.surface

    def calculate_perimiter(self):
        return self.surface * 4


# creating objects
rectangle = Rectangle(2, 4)
square = Square(4)
rectangle.width = 10  # changing the values of width in rectangles
square.surface = 10

print(f'Area of Square {square.calculate_area()}')
print(f'Perimeter of Square {square.calculate_perimiter()}')
print(f'Area of Rectangle {square.calculate_area()}')
print(f'Perimeter of Rectangle {square.calculate_perimiter()}')

print(rectangle.who_i_am())
print(square.who_i_am())