def is_pattern_contained_in_grid(grid, S):
    # Implement this placeholder.
# k, -> the length of the sequence, T[i][j][k] = T[i-1][j][k -1] or T[i+1][j][k-1] or ... and T[i][j] == grid[k]
    # T = [[[True] * (len(grid) + 1) for _ in range(len(grid[0]) + 1)] for _ in range(S) + 1]

    # for r in range(1, len(grid) + 1):
    #     for c in range(1, len(grid) + 1):
    #         for k in range(S):
    #             T[r][c][k] = grid[k] == T[r][c] and (T[r-1][c][k-1] or T[r+1][c][k-1] or T[r][c-1][k-1] or T[r][c+1][k-1])
    bad_path = set()

    def is_pattern_contain_to_k(r, c, k):
        if k == len(S):
            return True

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c, k) not in bad_path \
                and grid[r][c] == S[k] \
                and any([is_pattern_contain_to_k(next_r, next_c, k + 1) for next_r, next_c in ((r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1))]):
                    return True

        bad_path.add((r, c, k))
        return False

    return any([is_pattern_contain_to_k(r, c, 0) for r in range(len(grid)) for c in range(len(grid[0]))])


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
