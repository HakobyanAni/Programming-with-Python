######## while ########

number = int(input("input a number to count it's factorial "))
factorial = 1
while number != 1:
    factorial = factorial * number
    number = number - 1

print(factorial)


result = ""
while result != "exit":
    result = input("Please, type exit to exit ")
    if result == 'exit':
        break

print(result)
# break - ends all cycle
# continue - ends only current iteration


counter = 4
while counter > 1:
    counter -= 1
    password = input("Please, enter your password.")
    if password == "1htd3kh":
        print("Access granted")
        break
else:   # if break in while works this else never works
    print("Access denied")



####### for ########
 
for i in range(8):
    print("i = ", i)

for i in range(3, 9):
    print("i = ", i)

for i in range(3, 10, 2):
    print("i = ", i)

for i in range(10, 5, -2):
    if i == 8:
        continue
    print("i = ", i)

# first argument is included in range but the last one doesn't.


for counter in range (3, 0, -1)
    password = input("Please, enter your password.")
    if password == "1htd3kh":
        print("Access granted")
        break
else:   # if break in for works this else never works
    print("Access denied")