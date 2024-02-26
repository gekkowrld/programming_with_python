#!/bin/python3

"""
A program to compute:
    - Area of a rectangle
    - Perimeter of a rectangle

The arguments to be passed:
    - lenght (int)
    - width (int)

"""


class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2*(self.lenght + self.width)


clen = int(input("Enter len: "))
win = int(input("Enter width: "))

rect = Rectangle(clen, win)
print("Area is: \n", rect.area())
print("Perimeter is: \n", rect.perimeter())
