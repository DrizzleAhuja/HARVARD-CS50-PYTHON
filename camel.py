def main():
    camel_case_name = input("Enter a variable name in camel case: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("Snake case:", snake_case_name)

def camel_to_snake(name):
    snake_name = []
    for char in name:
        if char.isupper():
            snake_name.extend(['_', char.lower()])
        else:
            snake_name.append(char)
    return ''.join(snake_name)

if __name__ == "__main__":
    main()
