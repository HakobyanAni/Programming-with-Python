# define a function which prints all the odd numbers between the given range
def print_odd_numbers(from_numb, to_numb):
    for i in range(from_numb, to_numb):
        if i % 2 != 0:
            print(i)

print_odd_numbers(3, 15)


# define a function which calculates factorial
def numb_factorial(number):
    factorial = 1
    while(number > 0):
        factorial = factorial * number
        number -= 1
    print(factorial)
 
numb_factorial(5)    # 120
numb_factorial(1)    # 1
numb_factorial(3)    # 6



# In Python all numbers are reference types
x = 7        # creates an object for 7 in memory
print(x)     # 7
print(id(x)) # 1403872528   - address in memory

x += 1       # creates a new object for 8 in memory
print(x)     # 8
print(id(x)) # 1403872544   - address in memory