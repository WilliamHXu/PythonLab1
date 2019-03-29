from numbers import Number
from typing import Any, List


def largest_in_list(list: List[Number]) -> Number:
    return max(list)


def reverse_list(list: List[Any]) -> List[Any]:
    result = []
    for i in range(len(list)):
        result.append(list[len(list) - i - 1])
    return result


def contains(element: Any, list: List[Any]) -> bool:
    for item in list:
        if item == element:
            return True
    return False


def every_other_list(list: List[Any]) -> List[Any]:
    result = []
    for i in range(len(list)):
        if i % 2 == 1:
            result.append(list[i])
    return result


def total(list: List[Number]) -> Number:
    sum = 0
    for element in list:
        sum += element
    return sum
