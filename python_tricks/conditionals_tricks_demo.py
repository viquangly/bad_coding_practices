
from typing import Optional


def check_credit_error(credit_score: Optional[int]) -> str:
    """
    Check the credit score of applicant.

    :param credit_score: optional; int.  If applicant has None for credit score, it means that they don't have a credit
    score established.

    :return: str
    """
    if credit_score < 700 or credit_score is None:
        return 'bad credit score'
    else:
        return 'good credit score'


check_credit_error(None)
check_credit_error(650)
check_credit_error(750)


def check_credit_verbose(credit_score: Optional[int]) -> str:
    if credit_score is None:
        return 'bad credit score'
    elif credit_score < 700:
        return 'bad credit score'
    else:
        return 'good credit score'


check_credit_verbose(None)
check_credit_verbose(650)
check_credit_verbose(750)


def check_credit_lazyeval(credit_score: Optional[int]) -> str:
    if credit_score is None or credit_score < 700:
        return 'bad credit score'
    else:
        return 'good credit score'


check_credit_lazyeval(None)
check_credit_lazyeval(650)
check_credit_lazyeval(750)


def check_credit_ternary(credit_score: Optional[int]) -> str:
    return 'bad credit score' if credit_score is None or credit_score < 700 else 'good credit score'


check_credit_ternary(None)
check_credit_ternary(650)
check_credit_ternary(750)