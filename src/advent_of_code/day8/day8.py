import math
import re
from functools import reduce
from os.path import dirname

from advent_of_code.utils import helpers


def parse_map(map: list[str]) -> dict:
    parsed_map: dict = {}

    for i in range(len(map)):
        if i == 0:
            parsed_map.update({ 'directions': map[i] })
            continue
        if map[i] == '': continue

        line = re.split('\W+', map[i])
        parsed_map.update({ line[0]: (line[1], line[2]) })
    return parsed_map

def traverse_map_as_camel(desert_map: dict, node: str = 'AAA', traversals: int = 0, iteration: int = 1) -> int:
    for direction in desert_map['directions']:
        node_lookup = desert_map[node]

        if direction == 'L':
            node = node_lookup[0]
        elif direction == 'R':
            node = node_lookup[1]
        traversals += 1

        if node == 'ZZZ':
            return traversals
        if traversals == len(desert_map['directions']) * iteration:
            return traverse_map_as_camel(desert_map, node, traversals, iteration + 1)

    return traversals

def traverse_map_as_ghost(desert_map: dict, initial_nodes: list[str] = []) -> int:
    end_traversals = []
    initial_nodes = list(filter(lambda node: node.endswith('A'), list(desert_map.keys())))

    for i in range(len(initial_nodes)):
        traversal = traverse_node_as_ghost(desert_map, initial_nodes[i])
        end_traversals.append(traversal)

    return reduce(lambda x, y: math.lcm(x, y), end_traversals)

def traverse_node_as_ghost(desert_map: dict, node: str = 'AAA', traversals: int = 0, iteration: int = 1) -> tuple[str, int]:
    for direction in desert_map['directions']:
        node_lookup = desert_map[node]
        if direction == 'L':
            node = node_lookup[0]
        elif direction == 'R':
            node = node_lookup[1]
        traversals += 1

        if node.endswith('Z'):
            return traversals
        if traversals == len(desert_map['directions']) * iteration:
            return traverse_node_as_ghost(desert_map, node, traversals, iteration + 1)

    return traversals


if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/desert_map.txt'
    initial_input = helpers.read_input(input_file)

    desert_map = parse_map(initial_input)
    camel_traversals = traverse_map_as_camel(desert_map)
    ghost_traversals = traverse_map_as_ghost(desert_map)
    print(camel_traversals, ghost_traversals)
