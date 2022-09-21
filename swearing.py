import csv

# key value of censored words and their replacements
censored_words = {
    'f******': 'ucking',
    'f*****': 'ucks',
    'f*****': 'ucked',
    'f***': 'uck',
    's***': 'hit',
    's*******': 'hitting',
    's***': 'hitty',
    's****': 'hits',
    'n*****': 'iggas',
    'n****': 'igga',
    'b****': 'itch',
}

def replace_censored_words():
    with open('metadata.csv', 'r') as f:
        reader = csv.reader(f)
        metadata = list(reader)

    for row in metadata:
        for censored_word in censored_words:
            # make a new variable that is censored_word without any *
            first_letter = censored_word[0] + censored_words[censored_word]
            row[0] = row[0].replace(censored_word, first_letter)

    with open('metadata.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(metadata)

if __name__ == "__main__":
    replace_censored_words()