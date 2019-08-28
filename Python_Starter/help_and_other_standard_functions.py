# As Python is Object-oriented language, so functions are objects too 
# and they have their own attributes. Documentation lines are  
# saved in an attribute _doc_

doc_line_of_func_print = print.__doc__

print(doc_line_of_func_print)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.

print("************************")

def function_with_doc():
    """
    Documentation.
    Here can be a long description of the function definition.
    """
    print("Hello world !")

help(function_with_doc)    
# or
print(function_with_doc.__doc__)



# Other standard functions 

print(chr(98))          # cod 98 is symbol 'b'

print(bin(2))           # 0b1000 (binary version of 8)

print(ord('a'))         # code of 'a' symbol is 97

x = 2
print(callable(x))      # false
                        # true if parameter is a function or 
                        # it can be called as function, in other
                        # words, it is callable, otherwise false.

print(divmod(5,3))      # (1, 2)
                        # where 1 = 5 // 3
                        # and 2 = 5 % 3

print(hex(5))           # 0x5 - hexadecimal version of number 5

print(len("abcdefgh"))  # 8 - length of a given string

print(sorted("5891"))   # ['1', '5', '8', '9']

print(type(5))          # int
print(type('xf'))       # str


sequence = "12345"
def reverse_sequence(sequence):
    for i in reversed(sequence):
        print(i)

reverse_sequence(sequence)    # 5 4 3 2 1


def number_versions(number):
    print('Binary', bin(number))
    print('Octal', oct(number))
    print('Hexadecimal', hex(number))

print(max(5, 6, 10))    # 10
print(min(5, 8, 11))    # 5

