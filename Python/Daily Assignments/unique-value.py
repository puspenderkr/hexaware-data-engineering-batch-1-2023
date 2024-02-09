original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))

print(unique_list)

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)


original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = [item for item in original_list if original_list.count(item) == 1]

print(unique_list)


