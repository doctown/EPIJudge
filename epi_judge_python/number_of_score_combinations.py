"""
    w 2  3  7
    0 0  0  0
    1 2  3  7
    . 4  6  14
    . 6  9  21
    .
    12

score 0 1 2 3 4
    2 0 2 4 6
  2,3 0 3 6 9 12
2,3,7 0 5 10 0
    1 2  3  7
    . 4  6  14
    . 6  9  21
    .
    12

    T[i][j] =
"""


def num_combinations_for_final_score(final_score, individual_play_scores):
    T = [[0] * (final_score + 1) for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        T[i][0] = 1

    print(T)
    for i in range(len(individual_play_scores)):
        for score in range(1, final_score + 1):
            T[i][score] = sum(map(lambda val: T[i][score - val] if score - val >= 0 else 0, individual_play_scores[:i + 1]))

    print(T)
    return T[len(individual_play_scores) - 1][score]


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
