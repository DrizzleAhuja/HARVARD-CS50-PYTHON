def main():
    time_input = input("Enter the time in 24-hour format (HH:MM): ")
    converted_time = convert(time_input)

    if 7 <= converted_time < 8:
        print("breakfast time")
    elif 12 <= converted_time < 13:
        print("lunch time")
    elif 18 <= converted_time < 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
