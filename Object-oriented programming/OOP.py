class Person:
    first_name_field = "John"
    last_name_field = "Brown"
    age_field = 15

    def print_personal_info(self):
        print(self.first_name_field)
        print(self.last_name_field)
        print(self.age_field)


obj_1 = Person()
obj_2 = Person()

print(Person.first_name_field)     # John
print(Person.last_name_field)      # Brown
print(Person.age_field)            # 15

Person.first_name_field = "Helen"  # change the attribute first_name_field for all objects of that class (like global variable)
print(Person.first_name_field)     # Helen
print(obj_1.first_name_field)      # Helen
print(obj_2.first_name_field)      # Helen

obj_1.age_field = 25               # create a new attribute age_field only for obj_1
print(Person.age_field)            # 15
print(obj_1.age_field)             # 25
print(obj_2.age_field)             # 15


obj_1.print_personal_info()
# or
Person.print_personal_info(obj_1)