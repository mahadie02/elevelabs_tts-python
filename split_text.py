import re

def read_and_split_text(filename, character_limit):
    # Read text from file
    with open(filename, 'r') as file:
        text = file.read().replace('\n', ' ')
    
    words = text.split()[:5]
    title = ' '.join(words)
    title = re.sub(r'[.,;:!?]', '', title)

    # Count total characters
    total_characters = len(text)

    # Split text into chunks
    chunks = []
    start = 0
    while start < total_characters:
        end = start + character_limit
        if end >= total_characters:
            chunks.append(text[start:])
            break
        chunk_text = text[start:end]
        match = re.search(r'[.;:!?]', chunk_text[::-1])
        if match:
            split_index = end - match.start() - 1
            chunks.append(text[start:split_index + 1])
            start = split_index + 1
        else:
            chunks.append(chunk_text)
            start = end

    return title, chunks

