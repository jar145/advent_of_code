from functools import reduce
from os.path import dirname
from advent_of_code.utils import helpers

initial_load = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

replacements = (':', ''), (';', ''), (',', '')

def get_numbers_before_word(input_string: list[str], word_to_find: str) -> list[int]:
    return [int(input_string[idx-1]) for idx, word in enumerate(input_string) if word == word_to_find]

def remove_str_characters(input: str, characters_to_remove: dict) -> str:
    return reduce(lambda a, kv: a.replace(*kv), characters_to_remove, input)

def check_games(initial_list: list[str]) -> list[int]:
    valid_games: list[int] = []
    for game in initial_list:
        split_game = remove_str_characters(game, replacements).split(' ')
        red = get_numbers_before_word(split_game, 'red')
        green = get_numbers_before_word(split_game, 'green')
        blue = get_numbers_before_word(split_game, 'blue')

        if ((all(i <= initial_load['red'] for i in red)) and
            (all(i <= initial_load['green'] for i in green)) and
            (all(i <= initial_load['blue'] for i in blue))):
            valid_games.append(int([split_game[idx+1] for idx, word in enumerate(split_game) if word == "Game"][0]))
            continue

    return valid_games

def fewest_in_games(initial_list: list[str]) -> list[int]:
    product_of_fewest: list[int] = []
    for game in initial_list:
        split_game = remove_str_characters(game, replacements).split(' ')
        red = sorted(get_numbers_before_word(split_game, 'red'), reverse=True)
        green = sorted(get_numbers_before_word(split_game, 'green'), reverse=True)
        blue = sorted(get_numbers_before_word(split_game, 'blue'), reverse=True)

        product_of_fewest.append(red[0] * green[0] * blue[0])

    return product_of_fewest


if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/game_data.txt'

    doc = helpers.read_input(input_file)
    valid_games = check_games(doc)
    fewest_games = fewest_in_games(doc)
    sum_part1 = helpers.add_ints(valid_games)
    sum_part2 = helpers.add_ints(fewest_games)

    print()
