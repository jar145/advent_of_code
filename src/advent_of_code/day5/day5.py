from os.path import dirname

from advent_of_code.utils import helpers
from advent_of_code.utils.DictList import Dictlist

def build_map(almanac: list[str]) -> dict:
    parsed_almanac = parse_almanac(almanac)
    print('map parsed')
    range_map = get_range_map(parsed_almanac)
    return range_map

def get_range_map(initial_mappings: dict) -> dict:
    range_map = Dictlist()
    sorted_range_map = Dictlist()
    for map in initial_mappings:
        print(map)
        if 'seeds' in map:
            range_map.update({ 'seeds': initial_mappings['seeds'] })
            continue

        for listing in initial_mappings[map]:
            source, destination, increment = listing[1], listing[0], listing[-1]
            source_range = [range(source, source + increment)]
            destination_range = [range(destination, destination + increment)]

            if map in range_map.keys():
                range_map[map][0][0:0] = source_range
                range_map[map][1][0:0] = destination_range
            else:
                range_map[map] = source_range
                range_map[map] = destination_range

    print('sorting map...')
    sorted_range_map = parallel_sort(range_map)
    print('map sorted')

    return sorted_range_map

def parallel_sort(range_map: Dictlist) -> Dictlist:
    sorted_range_map = Dictlist()
    for map in range_map:
        if map == 'seeds':
            sorted_range_map.update({ 'seeds': range_map['seeds'] })
            continue

        source_map = range_map[map][0]
        destination_map = range_map[map][1]
        sorted_destination_map = [x for _,x in sorted(zip(source_map,destination_map), key=lambda r: r[0].start)]
        sorted_source_map = sorted(range_map[map][0], key=lambda r: r.start)
        sorted_range_map[map] = sorted_source_map
        sorted_range_map[map] = sorted_destination_map
    return sorted_range_map


def consolidate_map(range_map: Dictlist) -> list[list[int]]:
    range_list: list[list[int]] = []
    for map in range_map:
        if map == 'seeds':
            continue
        for listing in range_map[map]:
            range_list.append(listing)
    print('map consolidated')
    return range_list


def get_map_traversals(range_map: Dictlist) -> list[int]:
    traversals: list[int] = []
    seed_values = range_map['seeds']
    range_list = consolidate_map(range_map)
    location: int

    for seed in seed_values:
        print()
        print(f'-> seed: {seed}')
        initial_index = 0
        which_area: int
        location: int = seed

        range_iter = iter(range(initial_index, len(range_list)))
        for i in range_iter:
            if i % 2 == 0:
                for area in range_list[i]:
                    if location in area:
                        location = location - area.start
                        print(f'      {location}')
                        which_area = range_list[i].index(area)
                        break

                    if area == range_list[i][-1]:
                        helpers.consume(range_iter, 1)
                        print(f'dest: {location}')
                        break
                continue

            else:
                area = range_list[i][which_area]
                location = area.start + location
                print(f'dest: {location}')

        traversals.append(location)
    return traversals


def parse_almanac(almanac: list[str]) -> list[str]:
    map = Dictlist()
    for i in range(len(almanac)):
        if 'seeds:' in almanac[i]:
            map.update({ 'seeds': [int(element) for element in almanac[i].split() if element.isdigit()] })
        elif 'seed-to-soil map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['seed-to-soil'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'soil-to-fertilizer map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['soil-to-fertilizer'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'fertilizer-to-water map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['fertilizer-to-water'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'water-to-light map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['water-to-light'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'light-to-temperature map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['light-to-temperature'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'temperature-to-humidity map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['temperature-to-humidity'] = [int(element) for element in almanac[j].split() if element.isdigit()]
        elif 'humidity-to-location map:' in almanac[i]:
            for j in range(i + 1, len(almanac)):
                if almanac[j] == '':
                    i = j
                    break;
                map['humidity-to-location'] = [int(element) for element in almanac[j].split() if element.isdigit()]
    return map


if __name__ == '__main__':
    input_file = f'{dirname(__file__)}/almanac.txt'

    almanac = helpers.read_input(input_file)
    print('almanac read successfully')
    map = build_map(almanac)
    print('map built')
    traversals = get_map_traversals(map)
    print('map traversed')
    nearest_location = min(traversals)
    print(nearest_location)
