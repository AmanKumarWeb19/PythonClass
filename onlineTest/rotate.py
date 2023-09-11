# Write a Python function that rotates an array to the right by a given number of steps. 
# For example, if you have an array [1, 2, 3, 4, 5] and you want to rotate it to the right by 2 steps, 
# the result should be [4, 5, 1, 2, 3].

def rotate_array(arr, steps):
    # Calculate the effective number of steps to avoid unnecessary rotations
    effective_steps = steps % len(arr)
    
    # Slice the array to perform the rotation
    rotated_array = arr[-effective_steps:] + arr[:-effective_steps]
    
    return rotated_array

# Test case
original_array = [1, 2, 3, 4, 5]
steps_to_rotate = 2
result = rotate_array(original_array, steps_to_rotate)
print(result)  # Output: [4, 5, 1, 2, 3]
