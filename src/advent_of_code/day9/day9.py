import re
from os.path import dirname

from advent_of_code.utils import helpers

def parse_history(map: list[str]) -> list[list[int]]:
    parsed_map = []

    for i in range(len(map)):
        line = re.split(' ', map[i])
        parsed_map.append([int(element) for element in line if element])
    return parsed_map

def find_differences(row: list[int]) -> list[int]:
    differences = []
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        differences.append(diff)

    return differences

def find_all_differences(listing: list[int]) -> list[list[int]]:
    diff_list = []
    diff = find_differences(listing)
    diff_list.append(diff)

    while not all(i == 0 for i in diff):
        diff = find_differences(diff)
        diff_list.append(diff)

    diff_list.insert(0, listing)
    return diff_list

def calculate_next_item(listings: list[list[int]]) -> int:
    diff = 0

    for i in reversed(range(1, len(listings))):
        diff = diff + listings[i - 1][-1]

    return diff

def calculate_projections(history: list[int]) -> list[int]:
    projection_list = []

    for listing in history:
        diffs = find_all_differences(listing)
        projection = calculate_next_item(diffs)
        projection_list.append(projection)

    return projection_list


if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/environment_history.txt'

    history = parse_history(helpers.read_input(input_file))
    projections = calculate_projections(history)
    projectsion_sum = sum(projections)

    reversed_history = [sublist[::-1] for sublist in history]
    reversed_projections = calculate_projections(reversed_history)
    reversed_projectsion_sum = sum(reversed_projections)
    print(projectsion_sum, reversed_projectsion_sum)
