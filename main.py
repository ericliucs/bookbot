from collections import Counter


def count_words(book: str) -> int:
    return len(book.split())


def count_nonduped_chars(book: str) -> Counter[str]:
    return Counter(book.lower())


def make_alphabet_report(book_path: str) -> str:
    character_report = f"--- Begin report of {book_path} ---"

    with open(book_path) as book_file:
        book = book_file.read()
        num_chars = count_words(book)
        char_counts = count_nonduped_chars(book)
        alphabet_report_counts = make_alphabet_report_counts(char_counts)

        character_report = "\n".join([character_report,
                                      f"{num_chars} words found in the "
                                      "document\n",
                                      alphabet_report_counts,
                                      "--- End report ---"])

    return character_report


def make_alphabet_report_counts(char_counts: Counter[str]) -> str:
    alphabet_report_strs = []
    for char, count in char_counts.most_common():
        if char.isalpha():
            alphabet_report_strs.append(f"The '{char}' character was found "
                                        f"{count} times\n")
    return "".join(alphabet_report_strs)[:-1]


def main():
    print(make_alphabet_report("books/frankenstein.txt"))

if __name__ == "__main__":
    main()
