def main():
    user_input = input("Enter an arithmetic expression (x y z): ")
    x, operator, z = user_input.split()

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    print(f"Result: {result:.1f}")

if __name__ == "__main__":
    main()
