def main():
    amount_due = 50  # Initial amount due is 50 cents

    while amount_due > 0:
        coin = int(input("Insert Coin: "))

        # Check if the inserted coin is an accepted denomination
        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

    if amount_due < 0:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")
    else:
        print("Enjoy your Coke!")

if __name__ == "__main__":
    main()
