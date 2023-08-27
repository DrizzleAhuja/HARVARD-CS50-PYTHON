import validators

def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(email):
    return validators.email(email)

if __name__ == "__main__":
    main()
