import sys

def get_book_text(filepath):
	with open(filepath) as book:
		text = book.read()
	return text

from stats import book_to_words, count_letters, report

def print_report(filepath, word_count, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for char_dict in sorted_chars:
		char = char_dict["char"]
		count = char_dict["count"]
		if char.isalpha():
			print(f"{char}: {count}")
	print("============= END ===============")



def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	text = get_book_text(filepath)
	word_count = book_to_words(text)
	letter_count = count_letters(text)
	sorted_chars = report(letter_count)
	print_report(filepath, word_count, sorted_chars)





main()
