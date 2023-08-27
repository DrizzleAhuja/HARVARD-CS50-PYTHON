import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # IPv4 pattern: #.#.#.# where each # is a number between 0 and 255
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    if re.match(ipv4_pattern, ip):
        groups = re.match(ipv4_pattern, ip).groups()
        for group in groups:
            if not (0 <= int(group) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
