# As Python is Object-oriented language, so functions are objects too 
# and they have their own attributes. So, documentation lines are  
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
    This can be long description of the function definition.
    """
    print("Hello world !")

help(function_with_doc)    
# or
print(function_with_doc.__doc__)


