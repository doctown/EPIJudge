import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
 "" a b a r
 ""
 a  T
 b    F   T
 a      T F
 r        F
"""


def decompose_into_dictionary_words(domain, dictionary):
    T = [[True] * (len(domain) + 1) for _ in range(len(domain) + 1)]

    for r in range(1, len(domain) + 1):
        for c in range(r, len(domain) + 1):
            word = domain[r-1:c]
            T[r][c] = word in dictionary and (any(T[i][r - 1] for i in range(1, r)) if r > 1 else True)

    print(any([T[i][len(domain)] for i in range(1, len(domain) + 1)]))
    return [any([T[i][len(domain)] for i in range(1, len(domain) + 1)])]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
