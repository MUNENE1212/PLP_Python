# Create empty list
my_list = []

# Append elements
my_list.append([10, 20, 30, 40])


# Insert 15 at position 1 (second position)
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print index of value 30
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")

# Print final list
print(f"Final list: {my_list}")