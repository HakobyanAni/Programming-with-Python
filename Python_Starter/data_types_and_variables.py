# int, bool, float, complex, str, list, tuple, NoneType...

number_1 = 8 
print(type(number_1))       # int

number_2 = 0o753
print(number_2)             # 491

number_3 = 0xA
print(number_3)             # 10 
print(type(number_3))       # int 

number_4 = True
print(type(number_4))       # bool

number_5 = 1.859
print(type(number_5))       # float

string_1 = "15"
print(type(string_1))       # str

string_2 = '15'
print(type(string_2))       # str


# complex numbers
numb_1 = complex(2, 1)
print(numb_1)               # (2 + 1j)

numb_2 = 5 + 7j
print(numb_2)               # (5 + 7j)


# convert string to int
string_to_int = int(string_1)
print(string_to_int)        # 15
print(type(string_to_int))  # int


# operations between int, bool, string
variable_number = 5
variable_true = True
variable_false = False
variable_string = '8'
variable = variable_number + variable_true
print(variable)             # 6

variable = variable_number + variable_false
print(variable)             # 5

# variable = variable_number + variable_string
# print(variable)           # error


# dynamic typing
var = 5
print(var)                  # 5
print(type(var))            # int

var = 'qwerty'
print(var)                  # qwerty
print(type(var))            # string
