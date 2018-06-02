def get_max_trapped_water(heights):
    start_index, end_index = (0, len(heights) - 1)
    max_water_depth = float('-inf')

    while start_index < end_index:
        min_level = min(heights[start_index], heights[end_index])
        depth = calculate_depth(start_index, end_index, min_level)

        if depth > max_water_depth:
            max_water_depth = depth
        if heights[start_index] <= heights[end_index]:
            start_index += 1
        else:
            end_index -= 1

    return max_water_depth


def calculate_depth(start, end, level):
    return abs(end - start) * level



from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.tsv",
                                       get_max_trapped_water))
