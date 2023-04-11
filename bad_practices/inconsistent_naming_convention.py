
from typing import List


def calculate_total_amount(amts: List[float], discount: float, tax: float) -> float:
    total_amnt = sum(amts)
    if discount is not None:
        discounted_amt = (total_amnt * discount)
        total_amnt -= discounted_amt
    return total_amnt * (1 + tax)
