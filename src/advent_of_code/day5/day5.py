from os.path import dirname

from advent_of_code.utils import helpers
from advent_of_code.utils.DictList import Dictlist

def build_map(almanac: list[str]) -> dict:
    parsed_almanac = parse_almanac(almanac)
    range_map = get_range_map(parsed_almanac)
    return range_map

def get_range_map(initial_mappings: dict) -> dict:
    range_map = Dictlist()

    for map in initial_mappings:
        if 'seeds' in map:
            seed_range_iter = iter(range(len(initial_mappings[map])))
            for i in seed_range_iter:
                range_map[map] = range(initial_mappings[map][i], initial_mappings[map][i] + initial_mappings[map][i + 1])
                helpers.consume(seed_range_iter, 1)
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

    return parallel_sort(range_map)

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

    return range_list


def get_map_traversals(range_map: Dictlist) -> list[int]:
    traversals: list[int] = []
    seed_values = range_map['seeds']
    range_list = consolidate_map(range_map)

    for seed in seed_values:
        k = seed.start
        while k < seed.stop:
            seed = range(k, seed.stop)
            start_location: int = k
            stop_location: int = seed.stop
            print()
            print(f'-> seed: {seed}')
            which_area: int
            range_iter = iter(range(len(range_list)))
            for j in range_iter:
                if j % 2 == 0:
                    for area in range_list[j]:
                        if start_location in area and stop_location in area:
                            start_location = start_location - area.start
                            stop_location = stop_location - area.start
                            print(f'      ({start_location}, {stop_location})')
                            which_area = range_list[j].index(area)
                            break

                        if start_location in area and not stop_location in area:
                            start_location = start_location - area.start
                            range_difference =  abs(area.stop - stop_location)
                            stop_location = stop_location - area.start - range_difference
                            print(f'      ({start_location}, {stop_location})')
                            which_area = range_list[j].index(area)
                            break

                        if area == range_list[j][-1]:
                            helpers.consume(range_iter, 1)
                            print(f'dest: ({start_location}, {stop_location})')
                            break
                    continue

                else:
                    area = range_list[j][which_area]
                    start_location = area.start + start_location
                    stop_location = area.start + stop_location
                    print(f'dest: ({start_location}, {stop_location})')

            if stop_location - start_location == 0:
                break

            k = k + (stop_location - start_location)
            traversals.append(range(start_location, stop_location))

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
    map = build_map(almanac)
    traversals = get_map_traversals(map)
    nearest_location = min([point for r in traversals for point in (r.start, r.stop)])
    print(nearest_location)
