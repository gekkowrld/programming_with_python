"""
A class to describe the calculate the perimeter of a circle and area.
The radius is initialized
"""

from math import pi as PI, pow


class Circle:
    def __init__(self, radius=7):
        self.radius = radius

    def area(self):
        return PI*pow(self.radius, 2)

    def perimeter(self):
        return PI*(self.radius*2)


radius = float(input("Enter the radius of the circle: "))
circ = Circle(radius)
print(f"The area of a circle of radius {radius} is {circ.area()}")
print(
    f"The circumference of a circle of radius {radius} is {circ.perimeter()}")
