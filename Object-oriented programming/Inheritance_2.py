# Another way to show base class and child class relations

class BaseClass(object):
    def descript_class(self):
        print("Method's class", __class__.__name__)
        print("Instance's class", type(self).__name__)

class ChildClass(BaseClass):
    pass


if __name__ == "__main__":
    base_instance = BaseClass()          # Method's class BaseClass
    base_instance.descript_class()       # Instance's class BaseClass

    child_instance = ChildClass()        # Method's class BaseClass
    child_instance.descript_class()      # Instance's class ChildClass