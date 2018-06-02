import re
my_dict = 'pg29765.txt'
dest = 'cleaned.txt'
identifier = ';'
p = re.compile('[A-Z-]+')

def extract_words(original_path, dest_path):
    with open(original_path, 'r') as dictionary:
        lines = dictionary.readlines()

    words_txt = open(dest, 'w')
    for line in lines:
        word = extract_word(line)
        if word:
            words_txt.write(format_word(word))
    words_txt.close()

def extract_word(string):
    string = string.strip()
    m = p.match(string)
    string = string.partition(identifier)[0]
    if m and m.group() == string:
        return m.group().strip()
    return False

def format_word(string):
    return string.replace('-', '').lower() + "\r\n"

if __name__ == '__main__':
    extract_words(my_dict, dest)
