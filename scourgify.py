import sys
import csv

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, "r") as input_file, open(output_filename, "w", newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # Write header row to output file
            writer.writerow(["first", "last", "house"])

            # Skip the header row in the input file
            next(reader)

            for row in reader:
                name = row[0]
                house = row[1]

                # Split the name into first name and last name
                first_name, last_name = split_name(name)

                # Write the formatted data to the output file
                writer.writerow([first_name, last_name, house])

        print(f"File '{output_filename}' created successfully!")

    except FileNotFoundError:
        print(f"Could not read {input_filename}")
        sys.exit(1)

def split_name(name):
    # Remove quotes and split the name into first name and last name
    name = name.strip('"')
    first_name, last_name = name.split(", ")
    return first_name, last_name

if __name__ == "__main__":
    main()
