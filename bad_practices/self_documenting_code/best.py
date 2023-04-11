
excellent_credit_threshold = 780
good_credit_threshold = 650
excellent_income_amount_ratio_threshold = 10
good_income_amount_ratio_threshold = 5


def approve_immediately(credit_score: int, income_amount_ratio: float, has_cosigner: bool) -> bool:
    return any([
        has_cosigner,
        credit_score >= excellent_credit_threshold,
        income_amount_ratio >= excellent_income_amount_ratio_threshold
    ])


def approve_based_on_ratio(credit_score: int, income_amount_ratio: float) -> bool:
    if credit_score >= good_credit_threshold:
        return income_amount_ratio >= good_income_amount_ratio_threshold
    else:
        return income_amount_ratio >= excellent_credit_threshold


def approve_loan(loan_amount: int, credit_score: int, yearly_income: int, has_cosigner: bool) -> bool:
    income_amount_ratio = yearly_income / loan_amount
    return (
        approve_immediately(credit_score, income_amount_ratio, has_cosigner)
        or approve_based_on_ratio(credit_score, income_amount_ratio)
    )

