# factorial with recursion
def factorial(number):
    if number == 0:
        return 1
    else: 
        return number * factorial(number - 1)

number = 5
result = factorial(5)


# fibonacci with recursion
import functools
@functools.lru_cache(maxsize=None)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1 ) + fibonacci(n - 2)

for i in range(1, 100):
    print(fibonacci(i))


# hanoi with recursion
def hanoi(x, a, b, c):
    if x != 0:
        hanoi(x - 1, a, c, b)
        print("Move x ring from ", a, " to ", c)
        hanoi(x - 1, b, a, c)

hanoi(8, 'A', 'B', 'C')
#