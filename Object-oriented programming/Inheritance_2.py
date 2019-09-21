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

    child_instance_3 = ChildClass_3()
    print(ChildClass_3.__mro__)          # __mro__ shows Method resolution order
                                         # (<class '__main__.ChildClass_3'>, <class '__main__.ChildClass_2'>, 
                                         # <class '__main__.ChildClass_1'>, <class '__main__.BaseClass'>, <class 'object'>)