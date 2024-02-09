# Example of using a while loop as a control structure
num = 1
while num <= 5:
    print(num)
    num += 1

# For Loop
fruits = ["apple", "orange", "banana"]
for fruit in fruits:
    print(fruit)


# While Loop
count = 0
while count < 5:
    print(count)
    count += 1


# Nested Loop
for i in range(3):
    for j in range(2):
        print(i, j)


# Break, Continue & Pass
for i in range(5):
    if i == 3:
        break  # exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 2:
        continue  # skip the rest of the loop body when i is 2
    print(i)

for i in range(5):
    if i == 3:
        pass  # do nothing and continue with the next iteration
    print(i)
