from collections import Counter

grocery_list = []

# Keep taking input until EOF (Ctrl-D on UNIX-like systems)
try:
    while True:
        item = input()
        grocery_list.append(item.lower())  # Convert to lowercase for case-insensitivity
except EOFError:
    pass

# Count the occurrences of each item
item_counts = Counter(grocery_list)

# Sort and print the grocery list
for item, count in sorted(item_counts.items()):
    print(f"{count} {item.upper()}")
