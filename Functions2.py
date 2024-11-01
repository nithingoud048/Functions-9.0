# Write a function add(a, b, /) that only allows positional arguments. The function should return the sum of a and b.
# Write a function greet(*, name) that only accepts name as a keyword argument and returns a greeting message.
# Write a function describe_person(age, /, * name) that requires age as a positional-only argument and name as a keyword-only argument. The function should return a description
# Write a function that accepts any number of positional arguments and returns their product.
# Write a function that accepts any number of keyword arguments and iterate the List of Numbers By using While Loops.

def add(a, b, /):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

def greet(*, nithin):
    return f"Hello, {nithin}!"

message = greet(nithin="Alice")
print(message)  # Output: Hello, Alice!

def describe_person(age=20, /, *, nithin):
    return f"This person is {age} years old and their name is {nithin}."

description = describe_person(nithin="Alice")
print(description)  # Output: This person is 20 years old and their name is Alice.

description = describe_person(30, nithin="Bob")
print(description)  # Output: This person is 30 years old and their name is Bob.

def product(*args):
    if not args:  # Check if no arguments are passed
        return 0  # or return 1 if you prefer the multiplicative identity
    result = 1
    for num in args:
        result *= num
    return result

print(product(2, 3, 4))  # Output: 24
print(product(1, 5, 7, 2))  # Output: 70
print(product())  # Output: 0 or 1 (depending on your preference)

def iterate_keyword_lists(**kwargs):
    for key, num_list in kwargs.items():
        print(f"Processing list for '{key}':")
        
        index = 0
        while index < len(num_list):
            print(num_list[index])
            index += 1

# Example usage:
iterate_keyword_lists(
    list1=[1, 2, 3],
    list2=[4, 5, 6],
    list3=[7, 8, 9]
)

1
2
3
4
5
6
8
9
 
