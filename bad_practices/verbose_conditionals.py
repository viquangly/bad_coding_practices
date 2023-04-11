
from typing import List

def was_olympics_held_verbose(year: int) -> bool:
    if ((year % 4) == 0) and (year != 1944):
        return True
    else:
        return False


def was_olympics_held_notverbose(year: int) -> bool:
    return ((year % 4) == 0) and (year != 1944)


def is_list_empty_verbose(some_list: List) -> bool:
    if len(some_list) == 0:
        return True
    else:
        return False


def is_list_empty_better(some_list: List) -> bool:
    return len(some_list) == 0


def is_list_empty_bets(some_list: List) -> bool:
    return bool(some_list)
