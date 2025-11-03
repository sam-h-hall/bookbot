import sys
from stats import get_word_count, get_book_text, get_character_count, get_report

def main():
    if (len(sys.argv) < 2):
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_text = get_book_text(filepath)
        get_word_count(book_text)
        character_dict = get_character_count(book_text)
        get_report(filepath)

main()
