# Another way to show base class and child class relations

class BaseClass(object):
    def descript_class(self):
        print("Method's class", __class__.__name__)
        print("Instance's class", type(self).__name__)

class ChildClass_1(BaseClass):
    pass

class ChildClass_2(ChildClass_1):
    def descript_class(self):
        print("Method's class", __class__.__name__)

class  ChildClass_3(ChildClass_2):  
    pass   

if __name__ == "__main__":
    base_instance = BaseClass()          # Method's class BaseClass
    base_instance.descript_class()       # Instance's class BaseClass

    child_instance = ChildClass_1()      # Method's class BaseClass
    child_instance.descript_class()      # Instance's class ChildClass_1

    child_instance_2 = ChildClass_2()
    child_instance_2.descript_class()    # Method's class ChildClass_2

    child_instance_3 = ChildClass_3()
    print(ChildClass_3.__mro__)          # __mro__ shows Method resolution order
                                         # (<class '__main__.ChildClass_3'>, <class '__main__.ChildClass_2'>, 
                                         # <class '__main__.ChildClass_1'>, <class '__main__.BaseClass'>, <class 'object'>)


# Usage of super()
class Animal(object):
    def __init__(self):
        self.can_run = False
        self.can_fly = False
    
    def print_abilities(self):
        print(type(self).__name__ )
        print('can run - ', self.can_run)
        print('can fly - ', self.can_fly)
        print()

class Hourse(Animal):
    def __init__(self):
        super().__init__()   # if we didn't call super here, we won't have base class attributes in a child class
        self.can_run = True

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True

class Pegasus(Hourse, Bird):
    pass

if __name__=='__main__':
    
    animal_1 = Hourse()
    animal_1.print_abilities()

    animal_2 = Bird()
    animal_2.print_abilities()

    animal_3 = Pegasus()
    animal_3.print_abilities()

# Hourse
# can run -  True
# can fly -  False

# Bird
# can run -  False
# can fly -  True

# Pegasus
# can run -  True
# can fly -  True