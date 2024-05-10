#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """ Calculate the area of the square """
        return self.width * self.width  # Alternatively, use self.width ** 2

    def perimeter(self):
        """ Calculate the perimeter of the square """
        return 4 * self.width

    def __str__(self):
        """ String representation of the square """
        return f"Square(width={self.width}, height={self.height})"

if __name__ == "__main__":
    s = Square(width=12, height=12)  # Create a square with equal width and height for a perfect square
    print(s)                         # Output: Square(width=12, height=12)
    print("Area:", s.area())         # Output: Area: 144
    print("Perimeter:", s.perimeter())  # Output: Perimeter: 48

