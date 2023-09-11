# Question:
# Write a Python function that determines if two strings are anagrams of each other. 
# An anagram is a word or phrase formed by rearranging the letters of another, such as "listen" and "silent."
# Your function should return True if the two input strings are anagrams, and False otherwise.
def are_anagrams(str1,str2):
# Remove spaces and convert both strings to lowercase for accurate comparison
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
# Check if the lengths of the two strings are different; if they are, they can't be anagrams
    if len(str1) != len(str2):
     return False
# Create dictionaries to count the occurrences of each character in both strings
    char_count1 = {}
    char_count2 = {}
  # Populate the dictionaries with character counts from both strings

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
# Compare the dictionaries to check if the character counts are the same
    return char_count1 == char_count2


# Test cases
print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))    
print(are_anagrams("rail safety", "fairy tales"))