# Lambda function to square a number
square = lambda x: x**2

# Using the lambda function
result = square(5)
print("Result of square function:", result)

import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string to Python dictionary
data_dict = json.loads(json_string)

# Display the resulting dictionary
print("Parsed JSON Dictionary:")
print(data_dict)