import re

from os.path import dirname
from advent_of_code.utils import helpers

number_dict = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'thr3e',
    'four': 'fo4ur',
    'five': 'fi5ve',
    'six': 'si6x',
    'seven': 'sev7en',
    'eight': 'ei8ght',
    'nine': 'ni9ne',
}

def compile_ints(input_list: list[str]) -> list[str]:
    int_data: list[str] = []

    for i in input_list:
        for num in number_dict:
            i = i.replace(num, str(number_dict[num]))
        int_data.append(re.sub("[^0-9]", "", i))

    return int_data

def format_ints(input_list: list[str]) -> list[int]:
    int_data: list[int] = []
    for i in input_list:
        element_length = len(i)
        if element_length < 2:
            int_data.append(int(i + i))
        else:
            int_data.append(int(i[0] + i[element_length - 1]))

    return int_data


if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/input.txt'

    input = helpers.read_input(input_file)
    ints = compile_ints(input)
    formatted_ints = format_ints(ints)
    sum = helpers.add_ints(formatted_ints)

    print()
