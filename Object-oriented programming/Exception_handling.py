try:
   a_number = float('a = ')
   b_number = float('b =')
   print(a_number / b_number)
except ZeroDivisionError:
    print('Cannot divide a number on zero') 
except ValueError as error:
    print(type(error), error)    # if we input a string instead of number:
                                 # <class 'ValueError'> could not convert string to float: 'a = '
except Exception:
    pass
else:                            # code in this block works if no exception is raised
    pass                         # pass continues programm without raising an exception
finally:                         # code in this block works without waiting any exception is being raised or not
    print('Block finally')



# Working with destructor
class MyClass():
    def __del__(self):           # destructor
        print(self, 'is going to be deleted.')

instance = MyClass()             # <__main__.MyClass object at 0x000001DCCF9060C8> is going to be deleted.
del instance                     

instance = MyClass()             
print(id(instance))              # address of object in memory 1995477725960



# If any Exception raises in destructor then it is being ignored
class MySampleClass():
    def __del__(self):           
        print(self, 'is going to be deleted.')
        raise Exception

print('Creating object.')                    # Creating object.
obj_1 = MySampleClass()

print('Deleting reference of the object.')   # Deleting reference of the object.
del obj_1                                    # <__main__.MySampleClass object at 0x00000154DFA86688> is going to be deleted.
                                             # Exception ignored in: ..... info about exception

print('Done.')                               # Done.
