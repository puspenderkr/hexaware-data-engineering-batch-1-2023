
#Filter Data in Python Lists using filter and lambda:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(filtered_numbers))  # Output: [2, 4, 6, 8, 10]


# Using lamda() for sroting
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Bob', 'Alice', 'David', 'Charlie']


# Using map() with lambda 
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]



# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with lambda to filter even numbers
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)

# Converting the filtered result to a list
result_list = list(filtered_numbers)

# Displaying the result
print(result_list)



# Using reduce() with lambda 
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24


