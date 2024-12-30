import string

def main():
    print(read_char("books/frankenstein.txt"))

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
def read_word(filename):
    words = read_file(filename).lower().split()
    return words

def count_words(filename):
    return len(read_word(filename))

def read_char(filename):
    count_char = {}
    for char in string.ascii_lowercase:
        count_char[char] = 0

    for word in read_word(filename):
        for char in word:
            if char.isalpha():
                count_char[char] += 1

    return count_char
    
main()