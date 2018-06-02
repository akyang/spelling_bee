import sys
my_dict = 'words_alpha.txt'

def load_letters(letters):
    return list(letters.lower())

def find_words(letters):
    with open(my_dict) as dictionary:
        english_words = dictionary.read().split()
    words = []
    special_char = letters[0]
    for word in english_words:
        if len(word) > 3 and special_char in word and only_contains(word, letters):
            words.append(word);
    return words

def only_contains(container, permitted_items):
    return all([item in permitted_items for item in container])

if __name__ == '__main__':
    letters = load_letters(sys.argv[1])
    words = sorted(set(find_words(letters)))
    for word in words:
        print(word)
    print(len(words))
