class Car:
    def __init__(self):
        self.__private_attribute = 42   # private attribute starts with two underlines

    def get_private(self):
        return self.__private_attribute
    
    def set_private(self, value):
        if __private_attribute < 100:
            __private_attribute = value

obj = Car()
obj.get_private()

print(obj._Car__private_attribute)       # 42
# print(obj.__private_attribute)         wrong written format !


# Encapsulation with property decorator
class Celsius:
    def __init__(self, temperature = 0):
        self.__temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('Not possible!! The temperature is below -273!!!')
        else:
            self.__temperature = value

temperature_obj = Celsius()
obj.temperature_obj = 20
print(obj.temperature_obj)


# Any code that retrieves the value of temperature will automatically call temperature()
# instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value
# to temperature will automatically call temperature.setter. This is one of the 
# beautiful features in Python. We can see that temperature setter was called even 
# when we created an object.