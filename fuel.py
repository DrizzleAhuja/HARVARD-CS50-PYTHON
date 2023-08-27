def main():
    # Get user input for a fuel fraction
    fraction_input = input("Enter a fuel fraction in X/Y format: ")
    try:
        percentage = convert(fraction_input)
        print("Fuel percentage:", percentage, "%")
    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x > y:
            raise ValueError("X should be less than or equal to Y")
        if y == 0:
            raise ZeroDivisionError("Y cannot be 0")
        percentage = round((x / y) * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid input format")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
