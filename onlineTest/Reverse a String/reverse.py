
# Question: Reverse a String

# Write a Python function to reverse a given string. For example, if the input is "hello," the function should return "olleh."

input_str="hello"
def reverse_String(str):
    return str[::-1]

reversed_str=reverse_String(input_str)
print(reversed_str)