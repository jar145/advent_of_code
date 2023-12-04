from os.path import dirname
from advent_of_code.utils import helpers

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

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
                # why does there have to be duplicates?! D:
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
            spec_char_found = False
            row = location[0]
            first_col = location[1][0]
            last_col = location[1][-1]

            if row == 0 and first_col == 0:
                for i in range(row, row + 2):
                    if spec_char_found: break
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row == 0 and last_col == len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row == 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break

            elif row == len(schematic) - 1 and first_col == 0:
                for i in range(row - 1, row + 1):
                    if spec_char_found: break
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row == len(schematic) - 1 and last_col == len(schematic[row]) - 1:
                for i in range(row, row + 2):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row == len(schematic) - 1 and first_col != 0and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 1):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break

            elif row != 0 and first_col == 0:
                for i in range(row - 1, row + 2):
                    if spec_char_found: break
                    for j in range(first_col, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row != 0 and last_col == len(schematic[row]) - 1:
                for i in range(row - 1, row + 2):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 1):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break
            elif row != 0 and first_col != 0 and last_col != len(schematic[row]) - 1:
                for i in range(row - 1, row + 2):
                    if spec_char_found: break
                    for j in range(first_col - 1, last_col + 2):
                        element = schematic[i][j]
                        if element == '.' or element.isnumeric():
                            pass
                        else:
                            valid_placements.append(int(number))
                            spec_char_found = True
                            break

    return valid_placements



if __name__ == '__main__':
    schematic = load_file_as_matrix()
    number_placements = get_number_placements(schematic)
    valid_placements = get_valid_placements(schematic, number_placements)
    sum1 = helpers.add_ints(valid_placements)
    print()
