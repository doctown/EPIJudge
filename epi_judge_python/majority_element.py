def majority_search(stream):
    letters = {}
    max_letter_count = float('-inf')
    max_letter = None

    for letter in stream:
        letters[letter] = (letters.get(letter) or 0) + 1

        if max_letter_count < letters[letter]:
            max_letter_count = letters[letter]
            max_letter = letter
    return max_letter


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.tsv',
                                       majority_search_wrapper))
