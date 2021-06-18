import typing

print(dir(typing))

from typing import Dict, Tuple, List, Set


def example_function(l: List[str]) -> Set[str]:
    return {"one", l[0]}


print(example_function(["test", 1]))


def example_dict(d: Dict[str, int]):
    print(d)


print(example_dict({1: "1"}))
