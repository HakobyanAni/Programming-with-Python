class Person:
    age = 15

    def print_personal_info(self):                    
        print(self.first_name, self.last_name, "is", self.age)

Person.first_name = "John"
Person.last_name = "Brown"

print(Person.first_name)       # John
print(Person.last_name)        # Brown
print(Person.age)              # 15


obj_1 = Person()
obj_1.first_name = "Joe"
obj_1.last_name = "Efron"
obj_1.age = 1 

obj_2 = Person()
obj_2.first_name = "Hailey"
obj_2.last_name = "Hudgens"

Person.print_personal_info(obj_1)     # Joe Efron is 1
Person.print_personal_info(obj_2)     # Hailey Hudgens is 15

Person.first_name = "Vanessa"  
print(Person.first_name)     # Vanessa
print(obj_1.first_name)      # Joe
print(obj_2.first_name)      # Hailey

Person.age = 88              # change the attribute age for the obj_2 too (Person.age is like a global variable here).
print(Person.age)            # 88
print(obj_1.age)             # 1
print(obj_2.age)             # 88
 
obj_2.age = 30               # The attribute age is only changed for obj_2.
print(Person.age)            # 88
print(obj_1.age)             # 1
print(obj_2.age)             # 30


obj_1.print_personal_info()        # creates print_personal_info for the obj_1 of class
# or
Person.print_personal_info(obj_1)
# result of this methods is the same, but they have different addresses in memory.