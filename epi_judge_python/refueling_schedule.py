# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.

MILES_PER_GALLON = 20


def calculate_gallons_needed(distance):
    return distance // MILES_PER_GALLON


def calculate_max_distance(gallons):
    return gallons * MILES_PER_GALLON


def make_trip(gas, gallon, distance):
    return gas + gallon - calculate_gallons_needed(distance)


def move_forward(city_index, number_of_cities):
    return (city_index + 1) % number_of_cities


def travel(start_index, gallons, distances):
    not_finished = True
    city_index = start_index
    # start with no gas, fill-up, cover distance, check gas
    gas = make_trip(0, gallons[city_index], distances[city_index])
    city_index = move_forward(city_index, len(gallons))

    while city_index != start_index and not not_finished:
        if gas < 0:
            not_finished = False
        else:
            gas = make_trip(gas, gallons[city_index], distances[city_index])

        city_index = move_forward(city_index, len(gallons))

    print(gas, city_index, start_index)
    return not_finished


def find_ample_city(gallons, distances):
    possible = False

    gallons_sorted = [i[0] for i in sorted(enumerate(gallons), key=lambda x:x[1])]
    gallons_sorted.reverse()

    for city_index in gallons_sorted:
        possible = travel(city_index, gallons, distances)
        if possible:
            break

    return city_index if possible else 0


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.tsv',
                                       find_ample_city))
