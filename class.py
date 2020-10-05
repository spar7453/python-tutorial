class Rectangle:  # define parent class
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        # Called when object is about to be destroyed
        print(self.__class__.__name__, " is destroyed")

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(width = {self.width!r}, height = {self.height!r})')

    def __str__(self):
        return (f'width = {self.width} , ' f'height = {self.height}')

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, width, height):
        Rectangle.__init__(self, width, height)

    def is_square(self):
        return self.width == self.height


def check_rec():
    print("rectangle")
    rec = Rectangle(1, 2)
    print(rec)  # call rec.__str__ if __str__ is defined, otherwise call __repr__
    print(str(rec))  # equivalent ot print(rec)
    print(repr(rec))  # if rec is not defined, returns memory address
    # rec destroyed here


check_rec()
print("")


def check_square():
    print("square")
    square = Square(2, 2)
    print(square)  # call parent's method
    print(str(square))  # call parent's method
    print(repr(square))  # call parent's method
    print(f"square.is_square() = {square.is_square()}")  # child method
    print(f"square.area() = {square.area()}")  # parent method
    # rec destroyed here


check_square()

