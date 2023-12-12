from operator import countOf
from os.path import dirname

from advent_of_code.utils import helpers
from advent_of_code.utils.DictList import Dictlist

def sort_hands(card_bids: dict) -> list[dict]:
    hands_by_kind = Dictlist()

    for hand in card_bids:
        value_count = {}
        hand_bid_pair = { hand: card_bids[hand] }

        for char in hand:
            value_count[char] = value_count.get(char, 0) + 1

        if countOf(value_count.values(), 5) == 1:
            hands_by_kind['five_of_a_kind'] = hand
        elif countOf(value_count.values(), 4) == 1:
            hands_by_kind['four_of_a_kind'] = hand
        elif countOf(value_count.values(), 3) == 1 and countOf(value_count.values(), 2) == 1:
            hands_by_kind['full_house'] = hand
        elif countOf(value_count.values(), 3) == 1:
            hands_by_kind['three_of_a_kind'] = hand
        elif countOf(value_count.values(), 2) == 2:
            hands_by_kind['two_pair'] = hand
        elif countOf(value_count.values(), 2) == 1 or countOf(value_count.values(), 2) == 2:
            hands_by_kind['one_pair'] = hand
        else: # countOf(value_count.values(), 1) == 5:
            hands_by_kind['high_card'] = hand

    sort_hands_by_kind(hands_by_kind)
    combined = hands_by_kind['five_of_a_kind'] + \
            hands_by_kind['four_of_a_kind'] + \
            hands_by_kind['full_house'] + \
            hands_by_kind['three_of_a_kind'] + \
            hands_by_kind['two_pair'] + \
            hands_by_kind['one_pair'] + \
            hands_by_kind['high_card']

    return combined

def sort_hands_by_kind(hands_by_kind: Dictlist) -> Dictlist:
    sort_order = 'AKQJT98765432'

    for kind in hands_by_kind:
        hands_by_kind[kind].sort(key=lambda word: [sort_order.index(c) for c in word])

    return hands_by_kind

def calculate_winnings(card_bids: dict, sorted_hands: dict) -> int:
    hand_rank = len(sorted_hands)
    winnings = 0

    for hand in sorted_hands:
        winnings = winnings + (card_bids[hand] * hand_rank)
        hand_rank = hand_rank - 1

    return winnings

if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/card_bids.txt'
    card_bids = helpers.read_input(input_file)

    card_bids_dict = { key: int(value) for key, value in (hand.split() for hand in card_bids) }
    sorted_hands = sort_hands(card_bids_dict)
    winnings = calculate_winnings(card_bids_dict, sorted_hands)

    print(winnings)
