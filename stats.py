def book_to_words(text):
        words = text.split()
        number = len(words)
        return number

def count_letters(text):
	letter_count = {}
	for char in text:
		char = char.lower()
		if char in letter_count:
			letter_count[char] += 1
		else:
			letter_count[char] = 1
	return letter_count

def sort_by(letter_count):
	return letter_count["count"]

def report(letter_count):
	char_list =  [{"char" : char, "count" : count} for char, count in letter_count.items()]
	char_list.sort(reverse=True, key=sort_by)
	return char_list

