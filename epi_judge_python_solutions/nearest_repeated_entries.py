def find_nearest_repetition(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)
        word_to_latest_index[word] = i
    return nearest_repeated_distance if nearest_repeated_distance != float(
        'inf') else -1


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
