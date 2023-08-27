import sys
import pyfiglet

def print_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        font_name = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
    else:
        print_usage_and_exit()

    text = input("Enter a text: ")

    if font_name:
        try:
            font = pyfiglet.Figlet(font=font_name)
            print(font.renderText(text))
        except pyfiglet.FontNotFound:
            print("Invalid usage")
            sys.exit(1)
    else:
        font = pyfiglet.Figlet()
        print(font.renderText(text))

if __name__ == "__main__":
    main()
