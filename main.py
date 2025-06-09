from stats import count_words, count_char, sort_dictionary

def get_book_text(book):
    with open(book) as file:
        read_book = file.read()
        return read_book

def main():
    book_path = "books/frankenstein.txt"
    print_book = get_book_text(book_path)
    get_word_count = count_words(print_book)
    char_count = count_char(print_book)
    sorted_dict = sort_dictionary(char_count)
    print(get_word_count)
    print(sorted_dict)

main()

