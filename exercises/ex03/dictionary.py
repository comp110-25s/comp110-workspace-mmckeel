"""Megan M's Dictionary Functions Exercise!"""

__author__: str = "730556813"


def invert(input: dict[str, str]) -> dict[str, str]:
    """This function reverses the positions of the key and value in the dictionary"""
    switched: dict[str, str] = {}
    for key in input:
        switched_key: str = input[key]
        switched_value: str = key
        if switched_key in switched:
            raise KeyError("Keys may not be duplicated!")
        switched[switched_key] = switched_value
    return switched


def count(value: list[str]) -> dict[str, int]:
    """Counts number of times a value is listed, returns value and said number"""
    return_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(value):
        if value[idx] in return_dict:
            return_dict[value[idx]] += 1
        else:
            return_dict[value[idx]] = 1
        idx += 1
    return return_dict


def favorite_color(given: dict[str, str]) -> str:
    """Returns the most frequent favorite color between all individuals"""
    colors: list[str] = []
    for name in given:
        colors.append(given[name])
    number_count: dict[str, int] = count(colors)
    idx: int = 0
    return_color: str = ""
    for color in number_count:
        if number_count[color] > idx:
            idx = number_count[color]
            return_color = color
    return return_color


def bin_len(string_list: list[str]) -> dict[int, set[str]]:
    """Condenses and groups all values in dict by listing number of times present"""
    return_dict: dict[int, set[str]] = {}
    for string in string_list:
        if len(string) in return_dict:
            return_dict[len(string)].add(string)
        else:
            return_dict[len(string)] = set()
            return_dict[len(string)].add(string)
    return return_dict
