# Question:

# Write a Python function that removes duplicates from an array (or list) of elements while
# preserving the original order of the elements.


def remove_duplicates(arr):
    # Create an empty list to store unique elements
    unique_elements = []
    
    # Iterate through the input array
    for element in arr:
        # If the element is not in the unique_elements list, add it
        if element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements

# Test case
arr = [3, 2, 1, 2, 4, 3, 5, 6, 6, 5]
result = remove_duplicates(arr)
print(result)  # Output: [3, 2, 1, 4, 5, 6]
