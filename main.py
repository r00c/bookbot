import string

def main():
    print_format("books/frankenstein.txt")


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    

def read_word(filename):
    words = read_file(filename).lower().split()
    return words


def count_words(filename):
    return len(read_word(filename))


def count_chars(filename):
    chars = {}
    for char in string.ascii_lowercase:
        chars[char] = 0

    for word in read_word(filename):
        for char in word:
            if char.isalpha():
                chars[char] += 1

    return chars

def print_format(filename):
	print(f"--- Begin report of {filename} ---")
	print(f"{count_words(filename)} words found in the document")
	print("\n")
	for char, count in count_chars(filename).items():
		print(f"The {char} character was found {count} times")
	print("--- End report ---")
    
main()