import re
# Define the list of stop words
stop_words = set([
    'a', 'i', 'it', 'am', 'at', 'on', 'in', 'of', 'to', 'is', 'so', 'too',
    'my', 'the', 'and', 'but', 'are', 'very', 'here', 'even', 'from', 'them',
    'then', 'than', 'this', 'that', 'though'
])
# Function to stem a word
def stem(word):
    # Common endings to look for in stemming
    endings = ['s', 'es', 'ed', 'er', 'ly', 'ing']

    for ending in endings:
        if word.endswith(ending):
            return word[:-len(ending)]
    return word
# Initialize an empty dictionary to store the index
index = {}
# Read input lines
line_number = 1
while True:
    line = input()

    # Check if the line contains only a single full-stop to stop reading
    if line.strip() == ".":
        break

    # Remove punctuation and convert to lowercase
    line = re.sub(r'[.,:;!&\'\?]', '', line.lower())

    # Split the line into words
    words = line.split()

    for word in words:
        # Remove stop words
        if word not in stop_words:
            # Stem the word
            word = stem(word)

            # Add the word to the index
            if word not in index:
                index[word] = [line_number]
            elif line_number not in index[word]:
                index[word].append(line_number)

    line_number += 1
# Print the index
for word, line_numbers in index.items():
    print(f"{word}: {', '.join(map(str, line_numbers))}")
