
import collections
from itertools import islice


def read_input(dir: str) -> list[str]:
    project_data: list[str]
    with open(dir) as file:
        project_data = file.readlines()

    return [x.strip() for x in project_data]

def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)
