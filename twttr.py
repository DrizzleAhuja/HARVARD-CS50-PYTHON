def main():
    tweet = input("Enter your tweet: ")
    shortened_tweet = shorten(tweet)
    print("Shortened tweet:", shortened_tweet)

def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()
