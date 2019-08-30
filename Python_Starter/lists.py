# In Python lists are mutable types. We can give index to the lists, so
# list[0] will be the first element of the list and list[-1] will be the 
# last element of the list.

# list slicing - list[start index, end index, space]
new_list = [1, 5, 7, 8, 0, 3]     
sub_list_1 = new_list[1:4]           
sub_list_2 = new_list[1:-1:2]
sub_list_3 = new_list[-1:0:-1]
sub_list_4 = new_list[2:]
sub_list_5 = new_list[2::2]
sub_list_6 = new_list[:-2]
sub_list_7 = new_list[::-2]

print(new_list)          # [1, 5, 7, 8, 0, 3]
print(sub_list_1)        # [5, 7, 8]
print(sub_list_2)        # [5, 8]
print(sub_list_3)        # [3, 0, 8, 7, 5]
print(sub_list_4)        # [7, 8, 0, 3]
print(sub_list_5)        # [7, 0]
print(sub_list_6)        # [1, 5, 7, 8]
print(sub_list_7)        # [3, 8, 5]

print(len(new_list))     # 6 - length of list

variable = 1
if variable in new_list:        # in keyword checks if given variable or string is included in list
    print("number exists in the list")
else:
    print("number doesn't exist in the list")

# variable = 1 => true
# variable = 15 => false
# string = "abcde" 
# variable = abc => true
# variable = z => false

new_list.append(100)      # append adds an element to list
print(new_list)           # [1, 5, 7, 8, 0, 3, 100]


for element in new_list:
    if element % 2 == 0:
        print("even number -  ", new_list[element])    
    else:
        print("odd number -  ", element)         

print(new_list)


# All this we can do with strings also.
