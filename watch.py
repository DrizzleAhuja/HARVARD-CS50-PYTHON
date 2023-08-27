import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match YouTube URLs in the src attribute
    youtube_url_pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"'

    match = re.search(youtube_url_pattern, s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
