# # define a function which prints all the odd numbers between the given range
# def print_odd_numbers(from_numb, to_numb):
#     for i in range(from_numb, to_numb):
#         if i % 2 != 0:
#             print(i)

# print_odd_numbers(3, 15)


# # define a function which calculates factorial
# def numb_factorial(number):
#     factorial = 1
#     while(number > 0):
#         factorial = factorial * number
#         number -= 1
#     print(factorial)
 
# numb_factorial(5)    # 120
# numb_factorial(1)    # 1
# numb_factorial(3)    # 6



# # In Python all numbers are reference types
# x = 7        # creates an object for 7 in memory
# print(x)     # 7
# print(id(x)) # 1403872528   - address in memory

# x += 1       # creates a new object for 8 in memoryb
# print(x)     # 8
# print(id(x)) # 1403872544   - address in memory

print("---------------------------------------------")

print("""As in Python all types are reference types, so, when we define 
a variable equals to 5 and then b equals to a, first of all in memory is created
a space for number 5, then, as b is equal to 5 also and every number allocates in 
memory only one time, so we just give reference copy of a to b, that's why 
their address in memory is the same. \n """)
a = 5 
b = a
print(a)        # a = 5
print(b)        # b = 5
print(id(a))    # address a - 1784571120
print(id(b))    # address b - 1784571120

print("""Unlike other programming languages, in this interpreter language by
changing the value of variable a, the value of b is not being changed, because
program is run line by line, that's why their address in memory is not the same. \n""")
a = 7
print(a)        # a = 7
print(b)        # b = 5
print(id(a))    # address a - 1784571152
print(id(b))    # address b - 1784571120