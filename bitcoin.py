import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide a valid number of Bitcoins.")
        sys.exit(1)

    try:
        bitcoin_price = get_bitcoin_price()
        total_cost = num_bitcoins * bitcoin_price
        formatted_cost = format_currency(total_cost)
        print(f"The current cost of {num_bitcoins:.4f} Bitcoins is {formatted_cost} USD")
    except requests.RequestException:
        print("Error fetching Bitcoin price.")
        sys.exit(1)

def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    return data["bpi"]["USD"]["rate_float"]

def format_currency(amount):
    return "${:,.4f}".format(amount)

if __name__ == "__main__":
    main()
