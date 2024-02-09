# Introduction to Map & Map Methods
# Using a dictionary as a map
grades = {"Alice": 90, "Bob": 85, "Charlie": 92}
print(grades["Alice"])

# Using the map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

# Using the map() function to double each element in a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))