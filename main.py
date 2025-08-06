import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    text = get_book_text(filepath)
    num_words = str(get_word_count(text))
    char_dict = get_char_count(text)
    # print(get_char_count(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + num_words + " total words")
    print("--------- Character Count -------")
    get_sorted_dict(char_dict)
main()
