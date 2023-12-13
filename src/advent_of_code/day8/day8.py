from operator import countOf
from os.path import dirname
import re
import sys

from advent_of_code.utils import helpers
from advent_of_code.utils.DictList import Dictlist
sys.setrecursionlimit(100000)

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

# def traverse_map_as_ghost(desert_map: dict, nodes: list[str] = [], traversals: int = 0, iteration: int = 1) -> int:
#     # print(iteration)
#     if nodes == []:
#         nodes = list(filter(lambda node: node.endswith('A'), list(desert_map.keys())))

#     for node in nodes:
#         for direction in desert_map['directions']:
#             temp_nodes = []
#             if direction == 'L':
#                 for node in nodes:
#                     temp_nodes.append(desert_map[node][0])
#             elif direction == 'R':
#                 for node in nodes:
#                     temp_nodes.append(desert_map[node][1])
#             nodes = temp_nodes
#             traversals += 1

#         if all(node.endswith('Z') for node in nodes):
#             return traversals
#         if traversals == len(desert_map['directions']) * iteration:
#             return traverse_map_as_ghost(desert_map, nodes, traversals, iteration + 1)

#     return traversals

if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/desert_map.txt'
    initial_input = helpers.read_input(input_file)

    desert_map = parse_map(initial_input)
    camel_traversals = traverse_map_as_camel(desert_map)
    # ghost_traversals = traverse_map_as_ghost(desert_map)
    print(camel_traversals)
