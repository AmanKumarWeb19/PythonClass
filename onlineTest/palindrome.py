#  Check for Palindrome:

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for accurate comparison
    clean_string = ''.join(input_string.split()).lower()
    
    # Compare the cleaned string with its reverse
    return clean_string == clean_string[::-1]

# Test cases
string1 = "racecar"
string2 = "A man a plan a canal Panama"
string3 = "hello"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: True
print(is_palindrome(string3))  # Output: False
