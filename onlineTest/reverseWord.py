# Write a Python function that reverses the order of words in a given string. 
# A word is defined as a sequence of non-space characters separated by spaces.

def reverse_word_order(input_string):
    # Split the input string into words based on spaces
    words = input_string.split()
    
    # Reverse the order of the words and join them back into a string
    reversed_string = ' '.join(reversed(words))
    
    return reversed_string

# Test case
input_string = "Hello World"
result = reverse_word_order(input_string)
print(result)  # Output: "World Hello"
