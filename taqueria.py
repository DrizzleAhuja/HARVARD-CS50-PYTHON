def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            order = input("Enter an item: ").title()
            if order in menu:
                total_cost += menu[order]
                print(f"Total cost so far: ${total_cost:.2f}")
            else:
                print("Invalid item. Please enter a valid item from the menu.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
