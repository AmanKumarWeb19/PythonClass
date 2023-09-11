# Question:

# Write a Python function that finds the maximum number in an array of integers.


def find_maximum(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return None

    # Initialize the maximum to the first element of the array
    max_num = arr[0]

    # Iterate through the array to find the maximum
    for num in arr:
        if num > max_num:
            max_num = num

    return max_num

# Test cases
arr1 = [3, 7, 2, 8, 5]
arr2 = [-1, -5, -9, -2, -3]
arr3 = []

print(find_maximum(arr1))  # Output: 8
print(find_maximum(arr2))  # Output: -1
print(find_maximum(arr3))  # Output: None
