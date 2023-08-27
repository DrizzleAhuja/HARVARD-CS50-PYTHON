import re

# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Function to convert date to YYYY-MM-DD format
def convert_to_iso(date):
    parts = re.split(r'[ /,]', date)

    if len(parts) == 3:
        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])

            if month in range(1, 13) and day in range(1, 32) and year > 0:
                return f"{year:04d}-{month:02d}-{day:02d}"

    return None

# Function to validate user input date
def validate_date(date_string):
    if re.match(r'\d{1,2}/\d{1,2}/\d{4}', date_string):
        return True

    for month in months:
        if month in date_string:
            return True

    return False

# Main program loop
while True:
    user_input = input("Enter a date in month-day-year format or Month Day, Year format: ")

    if validate_date(user_input):
        iso_date = convert_to_iso(user_input)
        if iso_date:
            print(iso_date)
            break
        else:
            print("Invalid date format. Please try again.")
    else:
        print("Invalid date. Please try again.")
