def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	word = words[0]
	print word

def print_last_word(words):
	word = words[-1]
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	print_first_word(sentence)
	print_last_word(sentence)

def print_first_and_last_sorted(sentence):
	unsortedwords = break_words(sentence)
	sortedwords = sort_words(unsortedwords)
	print_first_word(sortedwords)
	print_last_word(sortedwords)