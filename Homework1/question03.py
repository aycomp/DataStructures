# Question 03 (%20)

import math

# Develop an inheritance hierarchy based upon the following Polygon class:

class Polygon:
    def __init__(self, sides):
        """Initialized with the lengths of the sides"""
        for s in sides:
            if s <= 0:
                raise ValueError('Side lengths must be positive')
        self._sides = sides
        self._name = "Polygon"

    def name(self):
        return self._name

    def area(self):
        """The area of an arbitrary polygon is unknown"""
        return 0.0 #placeholder

    def perimeter(self):
        total = 0.0
        for s in self._sides:
            total += s
        return total
    
# Implement classes Triangle and Parallelogram that extend this base
# class, with the obvious meanings for the area() and perimeter()
# methods. Also implement classes, IsoscelesTriangle,
# EquilateralTriangle, Rectangle, and Square, that have the
# appropriate inheritance relationships.
# the math module is already imported, you can use math.sqrt if needed

#Implement here
class Triangle(Polygon):
    def __init__(self, sides):
        self._sides = sides
        self._name = "Triangle"

    def area(self):
        #u cevrenin yarisi
        #alan=sqrt(u*(u-a)*(u-b)*(u-c))
        u = (self._sides[0] + self._sides[1] + self._sides[2]) / 2
        a = math.sqrt(u * (u-self._sides[0]) * (u-self._sides[1]) * (u-self._sides[2]))
        return a

    def perimeter(self):
        a = (self._sides[0] + self._sides[1] + self._sides[2])
        return a

class IsoscelesTriangle(Triangle):
    def __init__(self, sides):
        self._sides = sides
        self._name = "IsoscelesTriangle"

    def area(self):
        # u cevrenin yarisi
        # alan=sqrt(u*(u-a)*(u-a)*(u-b))
        u = (self._sides[0] + self._sides[0] + self._sides[1]) / 2
        a = math.sqrt(u * (u - self._sides[0]) * (u - self._sides[0]) * (u - self._sides[1]))
        return a

    def perimeter(self):
        a = (self._sides[0] + self._sides[0] + self._sides[1])
        return a

class EquilateralTriangle(Triangle):
    def __init__(self, sides):
        self._sides = sides
        self._name = "EquilateralTriangle"

    def area(self):
        # u cevrenin yarisi
        # alan=sqrt(u*(u-a)*(u-a)*(u-b))
        u = (self._sides[0] + self._sides[0] + self._sides[0]) / 2
        a = math.sqrt(u * (u - self._sides[0]) * (u - self._sides[0]) * (u - self._sides[0]))
        return a

    def perimeter(self):
        a = (self._sides[0] + self._sides[0] + self._sides[0])
        return a

class Parallelogram(Polygon):
    def __init__(self, sides):
        self._sides = sides
        self._name = "Parallelogram"

    def area(self):
        # yukseklik ve aci bilgisi olmadigindan hesaplanamadi
        return 'yukseklik ve aci bilgisi olmadigindan hesaplanamadi'

    def perimeter(self):
        a = (self._sides[0] + self._sides[1] + self._sides[2] + self._sides[3])
        return a

class Rectangle(Parallelogram):
    def __init__(self, sides):
        self._sides = sides
        self._name = "Rectangle"

    def area(self):
        a = self._sides[0] * self._sides[1]
        return a

    def perimeter(self):
        a = (self._sides[0] + self._sides[0] + self._sides[1] + self._sides[1])
        return a

class Square(Parallelogram):
    def __init__(self, sides):
        self._sides = sides
        self._name = "Square"

    def area(self):
        a = self._sides[0] * self._sides[0]
        return a
    #Note: ornek test verisindeki cevre sonucu(6.5) nin 2 ile carpilmasi gerektigi dusunulerek yapildi.
    #Dogru sonuc 13 olmali.
    def perimeter(self):
        a = 4 * self._sides[0]
        return a


# The following should work:
shapelist = [Polygon([1.0,4.5,3.1,3.3]),
             Triangle([3.4,5.3,4.2]),
             IsoscelesTriangle([4.1,1]),
             EquilateralTriangle([4.2]),
             Rectangle([5,4]),
             Square([3.25])]


for shape in shapelist:
    print('{0} Area: {1:.3f}  Perimeter: {2:.3f}'.format(shape.name(),
                                                           shape.area(),
                                                           shape.perimeter()))

# the above line should print out:

# Polygon Area: 0.000  Perimeter: 11.900
# Triangle Area: 7.135  Perimeter: 12.900
# IsoscelesTriangle Area: 2.035  Perimeter: 9.200
# EquilateralTriangle Area: 7.638  Perimeter: 12.600
# Rectangle Area: 20.000  Perimeter: 9.000
# Square Area: 10.562  Perimeter: 6.500
