def get_media_type(file_name):
    # Dictionary mapping file extensions to media types
    extensions_to_media = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Get the file extension from the input file name
    file_extension = file_name.lower().split('.')[-1]

    # Look up the media type in the dictionary
    media_type = extensions_to_media.get('.' + file_extension, 'application/octet-stream')

    return media_type

def main():
    file_name = input("Enter the file name: ")
    media_type = get_media_type(file_name)
    print(media_type)

if __name__ == "__main__":
    main()
