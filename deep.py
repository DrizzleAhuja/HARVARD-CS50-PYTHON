def main():
    user_input = input("What is the Answer to the Great Question? ")
    if user_input == "42" or user_input.lower() == "forty-two" or user_input == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
