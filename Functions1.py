# Sum of Two Numbers
# Write a function add(a, b) that takes two numbers as input and returns their sum.
# Example: add(3, 5) should return 8

# Odd or Even Checker
# Write a function is_even(n) that checks if a given number n is even. If it’s even, return True; otherwise, return False.
# Example: is_even(4) should return True, and is_even(7) should return False.

# String Length
# Write a function string_length(s) that returns the length of a given string s.
# Example: string_length("hello") should return 5.

# Character Counter
# Write a function count_character(s, char) that counts the occurrences of a character char in a string s.
# Example: count_character("banana", "a") should return 3.


def add(a, b):
    return a + b

# Example usage
result = add(3, 5)
print(result)  # Output: 8

def is_even(n):
    return n % 2 == 0

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

def string_length(s):
    return len(s)

print(string_length("hello"))  # Output: 5

def count_character(s, char):
    return s.count(char)

print(count_character("banana", "a"))  # Output: 3
