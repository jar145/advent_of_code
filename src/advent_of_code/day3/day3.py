import math
from os.path import dirname
from advent_of_code.day3.DictList import Dictlist

def load_file_as_matrix() -> list[list[str]]:
    input_file = f'{dirname(__file__)}/engine_schematic.txt'
    project_data: list[str]
    with open(input_file, 'r') as file:
        project_data = [[element for element in line.strip()] for line in file]

    return project_data

def get_number_placements(schematic: list[list[str]]) -> dict:
    # { number: (row, [col_indexes])}
    placement_dictionary = Dictlist()
    temp_num_str = ''
    temp_col_list = []

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            element = schematic[i][j]
            if element.isnumeric():
                temp_num_str = temp_num_str + element
                temp_col_list.append(j)
            else:
                placement_dictionary[temp_num_str] = (i, temp_col_list)
                temp_num_str = ''
                temp_col_list = []
        del placement_dictionary['']

    return placement_dictionary

def get_valid_placements(schematic: list[list[str]], placements: dict) -> list[int]:
    valid_placements: list[int] = []
    for number in placements:
        # { number: (row, [col_indexes])}
        for location in placements[number]:
            row = location[0]
            first_col = location[1][0]
            last_col = location[1][-1]

            # not used in the given dataset
            if row == 0 and first_col == 0:
                for i in range(row - 1, row + 2):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            # not used in the given dataset
            elif row == 0 and last_col == len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            elif row == 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            # not used in the given dataset
            elif row == len(schematic) - 1 and first_col == 0:
                for i in range(row - 1, row + 1):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            # not used in the given dataset
            elif row == len(schematic) - 1 and last_col == len(schematic[row]) - 1:
                for i in range(row - 1, row + 1):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            elif row == len(schematic) - 1 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 1):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            elif row != 0 and first_col == 0:
                for i in range(row - 1, row + 2):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            elif row != 0 and last_col == len(schematic[row]) - 1:
                # not sure why this nees to be row - 2, but it works 🤷‍♂️
                for i in range(row - 2, row + 2):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

            elif row != 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 2):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element != '.' and not element.isnumeric():
                            valid_placements.append(int(number))
                            break

    return valid_placements

def get_gear_coordinates(schematic: list[list[str]], placements: dict) -> dict:
    # { gear_coordinates (as tuple(x, y)): [adjacent numbers with gear]}
    gear_coordinates = Dictlist()
    for number in placements:
        # { number: (row, [col_indexes])}
        for location in placements[number]:
            row = location[0]
            first_col = location[1][0]
            last_col = location[1][-1]

            # not used in the given dataset
            if row == 0 and first_col == 0:
                for i in range(row - 1, row + 2):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[set(i, j)] = int(number)
                            break

            # not used in the given dataset
            elif row == 0 and last_col == len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[set(i, j)] = int(number)
                            break

            elif row == 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            # not used in the given dataset
            elif row == len(schematic) - 1 and first_col == 0:
                for i in range(row - 1, row + 1):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            # not used in the given dataset
            elif row == len(schematic) - 1 and last_col == len(schematic[row]) - 1:
                for i in range(row - 1, row + 1):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            elif row == len(schematic) - 1 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 1):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            elif row != 0 and first_col == 0:
                for i in range(row - 1, row + 2):
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            elif row != 0 and last_col == len(schematic[row]) - 1:
                # not sure why this nees to be row - 2, but it works 🤷‍♂️
                for i in range(row - 2, row + 2):
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

            elif row != 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 2):
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '*':
                            gear_coordinates[(i, j)] = int(number)
                            break

    return gear_coordinates

def calculate_gear_ratios(gear_coordinates: dict) -> list[int]:
    ratios: list[int] = []
    for coordinate in gear_coordinates:
        nums_at_coordinate = gear_coordinates[coordinate]
        if len(nums_at_coordinate) == 2:
            ratios.append(math.prod(nums_at_coordinate))

    return ratios


if __name__ == '__main__':
    schematic = load_file_as_matrix()
    number_placements = get_number_placements(schematic)
    valid_placements = get_valid_placements(schematic, number_placements)
    sum1 = sum(valid_placements)

    gear_coordinates = get_gear_coordinates(schematic, number_placements)
    gear_ratios = calculate_gear_ratios(gear_coordinates)
    sum_of_gear_ratios = sum(gear_ratios)
    print(sum1, sum_of_gear_ratios)
