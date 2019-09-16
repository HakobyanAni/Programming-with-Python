class Person:
    def greeting(self):
        print("Hello world!")

class Boy(Person):
    def greeting_boy(self):
        print("Hello from boy!")

object = Boy()
object.greeting()          # Hello world!
object.greeting_boy()      # Hello from boy!


####  Special characteristics of Python Inheritance  ####

# -> Constructors can be inherited.
class Shape:
    def __init__(self, side = 0):
        self.side = side

class Square(Shape):
    def draw(self):
        for i in range(self.side):
            print('+ ' * self.side)

class Triangle(Shape):
    def draw(self):
        for i in range(1, self.side + 1):
            print('+ ' * i)

# -> Multiple inheritance is allowed.
class Bird:
    def run(self):
        print("I'm running.")

class Horse:
    def fly(self):
        print("I'm flying.")
        
class Pegasus(Bird, Horse):
    pass

def main():
    square = Square(4)
    square.draw()             # + + + + 
                              # + + + + 
                              # + + + + 
                              # + + + + 
    print()
    
    triangle = Triangle(6)
    triangle.draw()           # +
                              # + +
                              # + + +
                              # + + + +
                              # + + + + +
                              # + + + + + +
    print()

    animal = Pegasus()
    animal.run()      # I'm running.
    animal.fly()      # I'm flying.

if __name__ == '__main__':
    main()