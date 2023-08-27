# Dictionary mapping codes to their corresponding emojis
emoji_dict = {
    ":1st_place_medal:": "🥇",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    # Add more codes and their corresponding emojis as needed
}

# Prompt the user for input
user_input = input("Type a string with codes/aliases: ")

# Replace codes/aliases with emojis
for code, emoji in emoji_dict.items():
    user_input = user_input.replace(code, emoji)

# Print the emojized version
print("Output:", user_input)
