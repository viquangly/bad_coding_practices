
def was_olympics_held_bad(year: int) -> bool:
    return ((year % 4) == 0) and (year != 1944)


def was_olympic_held_good(year: int) -> bool:
    year_olympics_cancelled_worldwar2 = 1944
    return ((year % 4) == 0) and (year != year_olympics_cancelled_worldwar2)
