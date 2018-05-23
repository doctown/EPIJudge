WHITE = 'W'
BLACK = 'B'


def explore(board, cell, visited):
    visited.add(cell)
    x, y = cell

    for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        next_cell = (next_x, next_y)
        if next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board[0]) and next_cell not in visited and board[next_x][next_y] == WHITE:
            explore(board, next_cell, visited)


def fill_surrounded_regions(board):
    visited = set()
    # Loop around edge, explore adding to visited
    for row in range(len(board)):
        if row == 0 or row == len(board) - 1:
            for col in range(len(board[0])):
                if board[row][col] == WHITE:
                    explore(board, (row, col), visited)
        else:
            if board[row][0] == WHITE:
                explore(board, (row, 0), visited)
            if board[row][len(board[0]) - 1] == WHITE:
                explore(board, (row, len(board[0]) - 1), visited)
            # map(lambda col: explore(board, (row, col), visited) if board[row][col] == WHITE else None, [0, len(board[0]) - 1])

    # go through middle and mark as white
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board[row][col] == WHITE and (row, col) not in visited:
                board[row][col] = BLACK

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
