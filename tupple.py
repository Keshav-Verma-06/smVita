my_tuple = (1, 2, 3, 4)

# 1. Convert to list, modify, then convert back
temp_list = list(my_tuple)
temp_list[1] = 99  # Change value at index 1
edited_tuple = tuple(temp_list)
print("Edited tuple:", edited_tuple)

# 2. Concatenate tuples to add elements
new_tuple = my_tuple + (5, 6)
print("Tuple after adding elements:", new_tuple)

# 3. Remove an element (by value)
temp_list = list(my_tuple)
temp_list.remove(2)
removed_tuple = tuple(temp_list)
print("Tuple after removing 2:", removed_tuple)

# 4. Slicing to create a new tuple
sliced_tuple = my_tuple[:2] + my_tuple[3:]
print("Tuple after slicing out index 2:", sliced_tuple)
