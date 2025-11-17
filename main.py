import sys
from stats import count_words, count_character, sort_list_of_dict

def main(book):
    if len(book) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(book[1])
    ld =  sort_list_of_dict(book[1])

    print("Analyzing book found at books/frankenstein.txt...")
    print("============ BOOKBOT ============")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for l in ld:
        print(f"{l['char']}: {l['num']}")
if __name__ == "__main__":
    main(sys.argv)