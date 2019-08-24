# /  operation always returns float
# //  operation always returns int
x = 3
y = 5

result = x / y
print(result)               # 0.6

result = x // y 
print(result)               # 0

y = 6.
result = print(x // y)      # 0.0

# pow(x, y)
x = 5
y = 2
z = pow(x, y)
print(z)                    # 25 
# or
z = x ** y
print(z)                    # 25


# abs(x)
number = abs(5)
print(number)               # 5

number = abs(-5.6)
print(number)               # 5.6


#complex(re, im)
number = complex(1, 9)
print(number)               # (1 + 9j)


#round(x), round(x, n)
x = 7.8715
round_x = round(x)
print(round_x)              # 8

round_x = round(x, 1)
print(round_x)              # 7.9

round_x = round(x, 2)
print(round_x)              # 7.87



import math
# math.trunc(x) - removes the decimal values from the expression 
# and returns the integer value.

# math.floor(x) - returns the closest integer value which is less
# than or equal to the expression.

# math.ceil(x) - returns the smallest integer value which is 
# greater than or equal to the expression.

x = 10.3574
numb_trunc = print(math.trunc(x))  # 10 
numb_floor = print(math.floor(x))  # 10 
numb_ceil = print(math.ceil(x))    # 11

# math.pi
print(math.pi)                  # 3.141592653589793
print(math.e)                   #  2.718281828459045
print(math.sin(math.pi / 4))    #  0.7071067811865475
print(math.sqrt(4))             # 2.0