def main():
	print(read_file("books/frankenstein.txt"))


def read_file(path):
	with open(path) as f:
		return f.read()

main()