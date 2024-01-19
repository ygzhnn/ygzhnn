from abc import ABC, abstractclassmethod

class Shape():
    """
        Shape = super class / abstract class
    """
    #abstract method
    @abstractclassmethod
    def area(): pass

    @abstractclassmethod
    def perimeter(): pass


    #overriding and polymorphism
    def toString(): pass


class Square(Shape):
    "Sub class"
    def __init__(self,edge) -> None:
        self.__edge = edge #encapsulation

    def area(self):
        result = self.__edge**2
        print("Square area:",result)

    def perimeter(self):
        result = self.__edge*4
        print("Square perimeter: ",result)

    def toString(self):
        print("Square edge ",self.__edge)


class Circle(Shape):
    "Sub class"

    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    
    def area(self):
        result = self.PI*self.__radius**2
        print("Circle area: ",result)

    
    def perimeter(self):
        result = 2*self.PI*self.__radius
        print("Circle perimeter: ",result)

    def toString(self):
        print("Circle radius: ",self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()
    