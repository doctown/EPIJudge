import collections
import copy
import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):

    def search(maze, cur, e):
        if cur == e:
            return [cur]

        if cur in visited:
            return None

        res = None
        visited.add(cur)

        right = Coordinate(cur.x + 1, cur.y)
        up = Coordinate(cur.x, cur.y + 1)
        left = Coordinate(cur.x - 1, cur.y)
        down = Coordinate(cur.x, cur.y - 1)

        if path_element_is_feasible(maze, cur, up):
            res = search(maze, up, e)
            if res is not None:
                res.insert(0, cur)
                return res
        if res is None and path_element_is_feasible(maze, cur, down):
            res = search(maze, down, e)
            if res is not None:
                res.insert(0, cur)
                return res
        if res is None and path_element_is_feasible(maze, cur, right):
            res = search(maze, right, e)
            if res is not None:
                res.insert(0, cur)
                return res
        if res is None and path_element_is_feasible(maze, cur, left):
            res = search(maze, left, e)
            if res is not None:
                res.insert(0, cur)
                return res

        return res

    visited = set()
    return search(maze, s, e)

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.tsv', search_maze_wrapper))
