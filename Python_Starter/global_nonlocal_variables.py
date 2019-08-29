def greet_function():
    global greet
    greet = "Hi!"
    print(greet)

greet = "Hello !"

print('With global keyword')
greet_function()  # Hi !
print(greet)      # Hi !

print('---------------------------')

def greet_function():
    greet = "Hi!"
    print(greet)

greet = "Hello !"

print('Without global keyword')
greet_function()  # Hi !
print(greet)      # Hello !



def outer_function():
    number = 25         # this is nonlocal variable

    def inner_function():
        nonlocal number # to be able to change the global variable we
                        # should write global keyword instead of nonlocal keyword.
        print(number)   # 25
        number = 19     # nonlocal variable number changed to 19
    
    print(number)       # 25
    inner_function()    # call inner_function
    print(number)       # 19

number = 10             # this is global variable
print(number)           # global variable - 10
outer_function()        # call outer_function 
print(number)           # 10