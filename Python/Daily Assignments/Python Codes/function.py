# Defining a simple function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
result = greet("Alice")
print(result)


# Function with default argument values
def power(base, exponent=2):
    return base ** exponent

print(power(3))          # Uses default exponent (2)
print(power(3, 3))       # Uses specified exponent (3)


# Function with keyword arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="John")

# Using special parameters - *args and **kwargs
def example_function(arg1, *args, kwarg1="default", **kwargs):
    print(arg1)
    print(args)
    print(kwarg1)
    print(kwargs)

example_function(1, 2, 3, kwarg2="custom")


# Using arbitrary argument lists
def add_numbers(*args):
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)
print(result)
