# Create a dictionary to store the fruit names and their corresponding calorie counts
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "banana": 105,
    "orange": 62,
    "grapes": 69,
    # Add more fruits and their calorie counts as needed
    "watermelon": 30,
    "pear": 100,  # Corrected the calorie count for pear
    "kiwifruit": 90,  # Corrected the entry for kiwifruit
}

# Prompt the user to input a fruit name
user_input = input("Enter a fruit: ").lower()  # Convert input to lowercase for case-insensitivity

# Check if the user's input is in the dictionary
if user_input in fruit_calories:
    calories = fruit_calories[user_input]
    print("Calories:", calories)
else:
    print("Fruit not found in the database.")
