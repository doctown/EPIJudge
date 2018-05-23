import collections


def valid(x, y, width, height):
    return x >= 0 and x < height and y >= 0 and y < width


def flip_color(x, y, image):
    color = image[x][y]
    q = collections.deque([(x, y)])
    image[x][y] = not color

    while q:
        x, y = q.popleft()

        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if next_x >= 0 and next_x < len(image) and next_y >= 0 and next_y < len(image[0]) and image[next_x][next_y] == color:
                image[next_x][next_y] = not color
                q.append((next_x, next_y))


def flip_color2(x, y, image):
    height, width = len(image), len(image[0])
    color = image[x][y]
    image[x][y] = not color

    if valid(x + 1, y, width, height) and image[x + 1][y] == color:
        flip_color(x + 1, y, image)
    if valid(x - 1, y, width, height) and image[x - 1][y] == color:
        flip_color(x - 1, y, image)

    if valid(x, y + 1, width, height) and image[x][y + 1] == color:
        flip_color(x, y + 1, image)
    if valid(x, y - 1, width, height) and image[x][y - 1] == color:
      flip_color(x, y - 1, image)
    # Implement this placeholder.
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('painting.tsv', flip_color_wrapper))
