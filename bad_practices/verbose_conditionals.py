
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


def is_list_empty_best(some_list: List) -> bool:
    return bool(some_list)


def get_email_domain_bad1(email: str, case: str) -> str:
    domain = email.split('@')[-1]
    return domain.upper() if case.lower() == 'upper' else domain


get_email_domain_bad1('bdsc@gmail.com', 'upper')
get_email_domain_bad1('bdsc@gmail.com', 'up')


def get_email_domain_bad2(email: str, upper_case: str) -> str:
    domain = email.split('@')[-1]

    if upper_case.upper()[0] == 'Y':
        return domain.upper()
    else:
        return domain


get_email_domain_bad2('bdsc@gmail.com', 'yes')
get_email_domain_bad2('bdsc@gmail.com', 'y')
get_email_domain_bad2('bdsc@gmail.com', 'no')


def get_email_domain_better(email: str, upper_case: bool) -> str:
    domain = email.split('@')[-1]
    return domain.upper() if upper_case else domain


get_email_domain_better('bdsc@gmail.com', True)
get_email_domain_better('bdsc@gmail.com', False)
