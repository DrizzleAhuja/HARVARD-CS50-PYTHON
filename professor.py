import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        question = f"{x} + {y} = "

        tries = 0
        while tries < 3:
            answer = input(question)
            try:
                answer = int(answer)
                if answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"The correct answer is {correct_answer}")

    print(f"Your score: {score} out of 10")

def get_level():
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in (1, 2, 3):
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid level.")

def generate_integer(level):
    try:
        digits = level
        x = random.randint(0, 10 ** digits - 1)
        y = random.randint(0, 10 ** digits - 1)
        return x, y
    except ValueError:
        raise ValueError("Level should be 1, 2, or 3.")

if __name__ == "__main__":
    main()
