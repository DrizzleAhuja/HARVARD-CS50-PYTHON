import random

def main():
    level = get_level()
    target_number = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Enter a positive integer level: "))
            if level <= 0:
                print("Please enter a positive integer.")
            else:
                return level
        except ValueError:
            print("Please enter a valid positive integer.")

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess <= 0:
                print("Please enter a positive integer.")
            else:
                return guess
        except ValueError:
            print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
