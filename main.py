def main():
	article = read_file("books/frankenstein.txt")
	print(article)
	print(word_count(article))

def read_file(path):
	with open(path) as f:
		return f.read()

def word_count(article):
	word = len(article.split())
	return word

main()