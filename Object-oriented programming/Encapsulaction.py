class Car:

    def __init__(self):
        self.__private_attribute = 42   # private attribute starts with two underlines
    
    def get_private(self):
        return self.__private_attribute

obj = Car()
obj.get_private()

print(obj._Car__private_attribute)       # 42
# print(obj.__private_attribute)         wrong written format !