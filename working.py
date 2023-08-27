import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = r'(\d{1,2}):(\d{2})\s*(AM|PM) to (\d{1,2}):(\d{2})\s*(AM|PM)'

    match = re.match(time_pattern, s)
    if match:
        start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()
        start_hour = int(start_hour)
        start_minute = int(start_minute)
        end_hour = int(end_hour)
        end_minute = int(end_minute)

        if start_meridiem == 'PM' and start_hour != 12:
            start_hour += 12
        elif start_meridiem == 'AM' and start_hour == 12:
            start_hour = 0

        if end_meridiem == 'PM' and end_hour != 12:
            end_hour += 12
        elif end_meridiem == 'AM' and end_hour == 12:
            end_hour = 0

        if start_hour > 23 or start_minute > 59 or end_hour > 23 or end_minute > 59:
            raise ValueError("Invalid time")

        return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"

    raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
