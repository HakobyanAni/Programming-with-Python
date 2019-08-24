# Every new programming language for developer needs to be started with "Hello world!" statement.)))
print("Hello world !")

first_variable = float(input("Input the first variable  "))
second_variable = float(input("Input the second variable  "))
operation = input("Input the operation  ")

result = None

if operation == '+':
    result = first_variable + second_variable
elif operation == '-':
    result = first_variable - second_variable
elif operation == '*':
    result = first_variable * second_variable
elif operation == '/':
    result = first_variable / second_variable 
else:
    result = "Not supported operation."

print(result)


# ternar operator
is_ready = True
message = "ready" if is_ready else "not ready yet"
print(message)