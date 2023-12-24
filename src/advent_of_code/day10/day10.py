import re
from os.path import dirname

from recordclass import RecordClass

from advent_of_code.utils import helpers


class Point(RecordClass):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    row: int
    column: int

    def move_up(self) -> tuple[int, int]:
        self.row -= 1
        return (self.row + 1, self.column)

    def move_down(self) -> tuple[int, int]:
        self.row += 1
        return (self.row - 1, self.column)

    def move_right(self) -> tuple[int, int]:
        self.column += 1
        return (self.row, self.column - 1)

    def move_left(self) -> tuple[int, int]:
        self.column -= 1
        return (self.row, self.column + 1)

def parse_pipes(map: list[str]) -> list[list[int]]:
    parsed_map = []

    for i in range(len(map)):
        line = re.split('', map[i])
        parsed_map.append([element for element in line if element])
    return parsed_map

def find_start(pipe_matrix: list[list[str]]) -> Point:
    return next(Point(i, color.index('S')) for i, color in enumerate(pipe_matrix) if 'S' in color)

def take_step(pipe_matrix: list[list[str]], position: Point, pipe_symbol: str, previous_position: tuple[int, int] | None) -> tuple[int, int]:
    if pipe_symbol == 'S':
        if position.row != 0:
            if pipe_matrix[position.row - 1][position.column] in ['|', '7', 'F']:
                return position.move_up()

        if position.column != len(pipe_matrix[position.row]):
            if pipe_matrix[position.row][position.column + 1] in ['-', 'J', '7']:
                return position.move_right()

        if position.row != len(pipe_matrix):
            if pipe_matrix[position.row + 1][position.column] in ['|', 'L', 'J']:
                return position.move_down()

        if position.column != 0:
            if pipe_matrix[position.row][position.column - 1] in ['-', 'L', 'F']:
                return position.move_left()

    elif pipe_symbol == '|':
        if position.row - 1 == previous_position[0]:
            return position.move_down()
        else:
            return position.move_up()

    elif pipe_symbol == '-':
        if position.column - 1 == previous_position[1]:
            return position.move_right()
        else:
            return position.move_left()

    elif pipe_symbol == 'L':
        if position.row - 1 == previous_position[0]:
            return position.move_right()
        else:
            return position.move_up()

    elif pipe_symbol == 'J':
        if position.row - 1 == previous_position[0]:
            return position.move_left()
        else:
            return position.move_up()

    elif pipe_symbol == '7':
        if position.column - 1 == previous_position[1]:
            return position.move_down()
        else:
            return position.move_left()

    elif pipe_symbol == 'F':
        if position.row + 1 == previous_position[0]:
            return position.move_right()
        else:
            return position.move_down()

    return None


def navigate(pipe_matrix: list[list[str]], position: Point) -> int:
    position = find_start(pipe_matrix)
    number_of_steps = 0
    next_position = None
    pipe_symbol = 'S'

    while(pipe_symbol != 'S' or number_of_steps == 0):
        next_position = take_step(pipe_matrix, position, pipe_symbol, next_position)
        pipe_symbol = pipe_matrix[position.row][position.column]
        number_of_steps += 1

    return number_of_steps



if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/pipe_map.txt'
    pipe_matrix = parse_pipes(helpers.read_input(input_file))
    position = find_start(pipe_matrix)
 
    number_of_steps = navigate(pipe_matrix, position)
    print(position, number_of_steps / 2)
