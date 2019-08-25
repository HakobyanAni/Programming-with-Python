
def print_odd_numbers(from_numb, to_numb):
    for i in range(from_numb, to_numb):
        if i % 2 != 0:
            print(i)
        i += 1

print_odd_numbers(3, 15)
