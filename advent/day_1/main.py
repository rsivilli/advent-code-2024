from typing import Tuple


def split_and_sort(input_str: list[str]) -> Tuple[list[int], list[int]]:
    list_1: list[int] = []
    list_2: list[int] = []
    for item in input_str:
        split_item = item.split()
        list_1.append(int(split_item[0]))
        list_2.append(int(split_item[1]))
    list_1.sort()
    list_2.sort()
    return list_1, list_2


def difference_lists(list_1: list[int], list_2: list[int]) -> list[int]:
    """calculate the distance between list 1 and list 2"""
    out: list[int] = []
    if len(list_1) != len(list_2):
        raise ValueError("Lists are not the same length")
    for i in range(len(list_1)):
        out.append(abs(list_1[i] - list_2[i]))
    return out


def split_and_map(input_str: list[str]) -> dict[int, int]:
    keys: set[int] = set()
    occurs: list[int] = []
    out: dict[int, int] = {}
    for item in input_str:
        key, occur = item.split()
        keys.add(int(key))
        occurs.append(int(occur))
    for val in occurs:
        if val in keys:
            out[val] = out.get(val, 0) + 1

    return out


def mult_and_sum(input_dict: dict[int, int]) -> int:
    running_sum = 0
    for key, value in input_dict.items():
        running_sum += key * value
    return running_sum


def solve_1(input_str: list[str]) -> int:
    """given the lines read in from a file, break into two ordered lists, find the distance between items and add them"""
    list_1, list_2 = split_and_sort(input_str)
    diff_list = difference_lists(list_1, list_2)
    return sum(diff_list)


def solve_2(input_str: list[str]) -> int:
    occur_map = split_and_map(input_str)
    return mult_and_sum(occur_map)
