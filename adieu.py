def main():
    names = []

    while True:
        try:
            name = input("Enter a name: ")
            names.append(name)
        except EOFError:
            break

    print_goodbyes(names)

def print_goodbyes(names):
    for i in range(len(names)):
        if i == 0:
            print(f"Adieu, adieu, to {names[i]}")
        elif i == 1:
            print(f"Adieu, adieu, to {names[i-1]} and {names[i]}")
        else:
            all_but_last = ", ".join(names[:i])
            print(f"Adieu, adieu, to {all_but_last}, and {names[i]}")

if __name__ == "__main__":
    main()
