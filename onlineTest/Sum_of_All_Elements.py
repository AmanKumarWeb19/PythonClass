# Calculate the Sum of All Elements in an Array:

# Write a Python function that calculates the sum of all elements in an array of integers.

arr1 = [3, 7, 2, 8, 5]
arr2 = [-1, -5, -9, -2, -3]
arr3 = []

def sumTotal(arr):
     # Initialize a variable to store the sum
    total=0

    for num in arr:
        total += num
    return total
    
    # Test cases

    
print(sumTotal(arr1))
print(sumTotal(arr2))
print(sumTotal(arr3))