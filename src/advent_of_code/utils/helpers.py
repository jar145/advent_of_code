

def read_input(dir: str) -> list[str]:
    project_data: list[str]
    with open(dir) as file:
        project_data = file.readlines()

    return [x.strip() for x in project_data]

def add_ints(input_list: list[int]) -> int:
    sum: int = 0
    for i in input_list:
        sum = sum + i
    return sum
