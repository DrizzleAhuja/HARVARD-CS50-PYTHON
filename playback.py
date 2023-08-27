def main():
    user_input = input("Enter a sentence: ")
    slowed_down_input = user_input.replace(" ", "...")
    print(slowed_down_input)

if __name__ == "__main__":
    main()
