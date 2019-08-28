def square_of_two_numbers(a, b):
    result = pow(a, 2) + 2 * a * b + pow(b, 2)
    return result

res = square_of_two_numbers(2, 3)
print(res)


# call of function
def personal_info(first_name = 'Helen', last_name='Pitt', age=15):
    print('first name: ', first_name, sep='\t')
    print('last name: ', last_name, sep='\t')
    print('age: ', age, sep='\t')

# 1st version
personal_info('John', 'Lenon', 25)

# 2nd version
personal_info(
     first_name='Teo',
     last_name='Brown',
      age=30,)

# 3rd version
personal_info(first_name='Joseph', age=35, last_name='Morgan')

# 4th version
personal_info()

# 5th version
personal_info(last_name='Kayer', first_name='Nahi')