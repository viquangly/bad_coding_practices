
def approve_loan(loan_amount, credit_score, yearly_income, has_cosigner):
    excellent_credit_threshold = 780
    good_credit_threshold = 650
    excellent_income_amount_ratio_threshold = 10
    good_income_amount_ratio_threshold = 5

    income_amount_ratio = yearly_income / loan_amount

    if any([
        has_cosigner,
        credit_score >= excellent_credit_threshold,
        income_amount_ratio >= excellent_income_amount_ratio_threshold
    ]):
        return True
    else:
        if credit_score >= good_credit_threshold:
            return income_amount_ratio >= good_income_amount_ratio_threshold
        else:
            return income_amount_ratio >= excellent_credit_threshold
