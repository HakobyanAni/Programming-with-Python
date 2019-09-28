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



def main():
    try:
        raise ValueError('value is not correct.')
    except ValueError as error:
        print('Exception:', error)
        raise
 
try: 
    main()
except ValueError:
    print('Detected value error.')

# Exception: value is not correct.
# Detected value error.



### __context__  (keeps old exception)
value_error = ValueError()
value_error.__context__ = ZeroDivisionError()
exception = Exception()
exception.__context__ = value_error
raise exception

# ZeroDivisionError
# During handling of the above exception, another exception occurred:
# ValueError
# During handling of the above exception, another exception occurred:
# ............
#     raise exception
# Exception



###  __cause__
a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError as error:
   raise ValueError('value is not correct') from error
   # raise ValueError('cannot divide number on zero') from None  -in thos case we can't have any information about old exception

# ....
#     result = a / b
# ZeroDivisionError: division by zero
# The above exception was the direct cause of the following exception:
# ............
#  raise ValueError('value is not correct') from error
# ValueError: value is not correct