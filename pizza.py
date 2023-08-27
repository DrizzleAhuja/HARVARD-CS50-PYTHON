pip install tabulate
import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        print("Usage: python pizza.py filename.csv")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            print_table(data)
    except FileNotFoundError:
        print(f"File {filename} not found")
        sys.exit(1)

def print_table(data):
    headers = data[0]
    table_data = data[1:]
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
