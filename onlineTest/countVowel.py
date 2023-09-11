def count_vowels(input_string):
    # Convert the input string to lowercase for accurate counting
    input_string = input_string.lower()
    
    # Define a set of vowels
    vowels = set("aeiou")
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through the string and count the vowels
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Test cases
string1 = "Hello, World!"
string2 = "Python is awesome"
string3 = "This is a test"

print(count_vowels(string1))  # Output: 3 (e, o, o)
print(count_vowels(string2))  # Output: 6 (o, i, e, i, a, e)
print(count_vowels(string3))  # Output: 4 (i, i, a, e)
