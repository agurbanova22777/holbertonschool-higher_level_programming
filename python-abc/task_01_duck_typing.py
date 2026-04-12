#!/usr/bin/python3
"""Shapes using ABCs + duck typing helper."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract shape interface."""

    @abstractmethod
    def area(self):
        """Return the shape area."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the shape perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter for any object that has area() and perimeter()."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(4, 5)

    shape_info(c)
    shape_info(r)
