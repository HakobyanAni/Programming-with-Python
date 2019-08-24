string_1 = 'string'
string_2 = "string" 

print(string_1, string_2)  # string string

string_3 = "Hello " \
        "World !"
print(string_3)    # Hello World !

string_3 = "Hello  \
        World !"
print(string_3)    # Hello          World !

string_3 = "Hello \n" \
        "World !"
print(string_3)    # Hello
                 # World !

multiline_string = """This py file is about
working with strings.
We had already learnt types
- int
- bool 
- float. """
print(multiline_string)   # This py file is about
                          # working with strings.
                          # We had already learnt types
                          # - int
                          #- bool
                          # - float.


# string concatenation
string_1 = "How are you? "
string_2 = "What is your name?"
concat_string = string_1 + string_2
print(concat_string)       # How are you? What is your name?


# string formatting   s % x
var = 'number = %d' % 109
print(var)       # number = 109

var = 'number = %f' % 109
print(var)       # number = 109.000000

var = 'number = %4.2f' % 109
print(var)       # number = 109.00

var = '%s = %d' % ('number', 10)
print(var)       # number = 10

var = 'I am {}'.format(10) + ' years old' 
print(var)       # I am 10 years old 

var = '{} = {}'.format("sqrt of 4", 2)
print(var)       # sqrt of 4 = 2