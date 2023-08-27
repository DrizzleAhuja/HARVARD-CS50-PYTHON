import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        print("Usage: python lines.py filename.py")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            code_lines = count_code_lines(lines)
            print(f"Number of lines of code: {code_lines}")
    except FileNotFoundError:
        print(f"File {filename} not found")
        sys.exit(1)

def count_code_lines(lines):
    code_lines = 0
    in_multiline_comment = False

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("'''") or line.startswith('"""'):
            in_multiline_comment = not in_multiline_comment

        if in_multiline_comment or line.startswith("#"):
            continue

        code_lines += 1

    return code_lines

if __name__ == "__main__":
    main()
