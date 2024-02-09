# Input and Output
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
print("You will be " + str(age + 5) + " in 5 years.")


# Introduction to Lists
numbers = [1, 2, 3, 4, 5]
print(numbers)

fruits = ["apple", "orange", "banana"]
print(fruits)

# List Methods and Slicing
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

fruits = ["apple", "orange", "banana"]
sliced_fruits = fruits[1:3]
print(sliced_fruits)