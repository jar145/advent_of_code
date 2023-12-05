import re

from os.path import dirname
from advent_of_code.utils import helpers
from advent_of_code.utils.DictList import Dictlist

def get_number_of_matches(game_list: list[str]) -> dict:
    num_of_matches: dict = {}
    for game in game_list:
        split_game = re.split(': |\| ', game)
        game_number = int(re.findall('\d+|$', split_game[0])[0])
        winning_numbers = set([int(element) for element in split_game[1].split()])
        my_numbers = set([int(element) for element in split_game[2].split()])
        num_of_matches[game_number] = len(winning_numbers.intersection(my_numbers))

    return num_of_matches

def calculate_game_points(num_of_matches: list[int]) -> list[int]:
    points_per_game: list[int] = []
    for game in num_of_matches:
        amount_in_common = num_of_matches[game]
        if amount_in_common > 0:
            points_per_game.append(pow(2, amount_in_common - 1))
        else:
            points_per_game.append(0)

    return points_per_game

def get_game_copies(game_matches: list[int]) -> Dictlist:
    copy_list = { key: 1 for key in range(1, len(game_matches) + 1) }
    game_index = 0
    for game in game_matches:
        game_points = game_matches[game]
        for i in range(0, copy_list[game]):
            for j in range(game + 1, game + game_points + 1):
                copy_list[j] = copy_list.get(j) + 1

    return copy_list

if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/scratch_cards.txt'

    games = helpers.read_input(input_file)
    num_of_matches = get_number_of_matches(games)
    game_points = calculate_game_points(num_of_matches)
    sum_of_points = sum(game_points)

    card_copies = get_game_copies(num_of_matches)
    card_count = sum(card_copies.values())
    print(sum_of_points, card_count)
