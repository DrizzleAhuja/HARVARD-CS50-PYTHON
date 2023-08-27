import sys
from datetime import datetime, date


def calculate_age_in_minutes(birthdate):
    today = date.today()
    birth_datetime = datetime.strptime(birthdate, "%Y-%m-%d")
    age_in_minutes = (today - birth_datetime.date()).days * 24 * 60
    return age_in_minutes


def convert_to_words(minutes):
    if minutes == 0:
        return "zero"

    units = ["", "thousand", "million", "billion", "trillion", "quadrillion"]
    words = []

    while minutes > 0:
        minutes_part = minutes % 1000
        if minutes_part > 0:
            words.append(convert_part_to_words(minutes_part) + " " + units[len(words)])
        minutes //= 1000

    return " ".join(reversed(words))


def convert_part_to_words(part):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if part < 10:
        return ones[part]
    elif 10 <= part < 20:
        return teens[part - 10]
    else:
        return tens[part // 10] + ("-" + ones[part % 10] if part % 10 > 0 else "")


def main():
    if len(sys.argv) != 2:
        print("Usage: python seasons.py YYYY-MM-DD")
        sys.exit(1)

    birthdate = sys.argv[1]
    try:
        age_in_minutes = calculate_age_in_minutes(birthdate)
        age_in_words = convert_to_words(age_in_minutes)
        print(age_in_words.capitalize() + " minutes")
    except ValueError:
        print("Invalid date format")
        sys.exit(1)


if __name__ == "__main__":
    main()
