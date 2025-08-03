import array as arr

# Using the array module for homogeneous data
my_array = arr.array('i', [1, 2, 3, 4, 5])
print(f"Array created using array module: {my_array}")

# Using a Python list (more common)
my_list = [10, 20, 30, 40, 50]
print(f"List created: {my_list}")

# Accessing elements by index
print(f"First element of list: {my_list[0]}")
print(f"Third element of array: {my_array[2]}")
