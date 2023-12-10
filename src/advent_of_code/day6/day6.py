import math
from os.path import dirname

from advent_of_code.utils import helpers

def calculate_distance(race_time: int, hold_time: int) -> int:
    velocity = hold_time
    return velocity*(race_time - hold_time)

if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/race_times.txt'
    input = helpers.read_input(input_file)

    race_times = [int(element) for element in input[0].split() if element.isdigit()]
    records = [int(element) for element in input[1].split() if element.isdigit()]

    race_distances = [[calculate_distance(time, hold_time) for hold_time in range(0, time)] for time in race_times]
    num_of_records_beat = [len([element for element in race_distances[i] if element > records[i]]) for i in range(len(race_distances))]
    error_margin = math.prod(num_of_records_beat)
    print(error_margin)

    new_race_time = int(''.join(x for x in input[0] if x.isdigit()))
    new_record = int(''.join(x for x in input[1] if x.isdigit()))

    new_race_distance = [calculate_distance(new_race_time, hold_time) for hold_time in range(0, new_race_time)]
    new_margin_of_error = len([element for element in new_race_distance if element > new_record])
    print(new_margin_of_error)
