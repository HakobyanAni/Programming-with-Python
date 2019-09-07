class Rectangle:
    def __init__(self, side_a, side_b):   # constructor
        self.side_a = side_a              # data attribute
        self.side_b = side_b
    
    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)

    def __str__(self):
        return "Rectangle's side_a is "+ str(self.side_a) + ", and side_b is " + str(self.side_b) + "."

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __repr__(self):
        return "Circle(%.1f)" % self.radius

    @classmethod                         # class method
    def from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle.__repr__())          # Rectangle(3.0, 4.0)
    # or 
    print(repr(rectangle))               # Rectangle(3.0, 4.0)
    
    print(type(rectangle.__repr__()))    # <class 'str'>

    print(rectangle.__str__())           # Rectangle's side_a is 3, and side_b is 4.
    # or
    string_of_rectangle = str(rectangle)  
    print(string_of_rectangle)           # Rectangle's side_a is 3, and side_b is 4.

    first_circle = Circle(1)
    print(first_circle)                  # Circle(1.0)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)                 # Circle(2.5)


main()


###     _str_()
# This method returns the string representation of the object. This method is called
# when print() or str() function is invoked on an object. This method must return the
# String object. If we don’t implement __str__() function for a class, then built-in
# object implementation is used that actually calls __repr__() function.

###     _repr_()
# Python __repr__() function returns the object representation. It could be any valid
# python expression such as tuple, dictionary, string etc. This method is called when 
# repr() function is invoked on the object, in that case, __repr__() function must return 
# a String otherwise error will be thrown.