# Write a Python function that checks if a given substring exists within a given string. 
# The function should return True if the substring is found, and False otherwise.

def is_substring(substring, string):
    # Check if the substring is in the string using the "in" operator
    if substring in string:
        return True
    else:
        return False

# Test cases
string1 = "Hello, World!"
substring1 = "World"
substring2 = "Python"

print(is_substring(substring1, string1))  # Output: True
print(is_substring(substring2, string1))  # Output: False
