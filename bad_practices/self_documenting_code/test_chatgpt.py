
import pytest
from best import *


# test for approve_immediately function
def test_approve_immediately():
    # Test if has_cosigner is True
    assert approve_immediately(credit_score=600, income_amount_ratio=20, has_cosigner=True) == True

    # Test if credit score is excellent
    assert approve_immediately(credit_score=800, income_amount_ratio=9, has_cosigner=False) == True

    # Test if income amount ratio is excellent
    assert approve_immediately(credit_score=600, income_amount_ratio=11, has_cosigner=False) == True

    # Test if all conditions fail
    assert approve_immediately(credit_score=600, income_amount_ratio=4, has_cosigner=False) == False


# test for approve_based_on_ratio function
def test_approve_based_on_ratio():
    # Test if credit score is excellent
    with pytest.raises(ValueError):
        approve_based_on_ratio(credit_score=800, income_amount_ratio=20)

    # Test if income amount ratio is good and credit score is good
    assert approve_based_on_ratio(credit_score=700, income_amount_ratio=6) == True

    # Test if income amount ratio is excellent and credit score is good
    assert approve_based_on_ratio(credit_score=700, income_amount_ratio=11) == True

    # Test if all conditions fail
    assert approve_based_on_ratio(credit_score=600, income_amount_ratio=4) == False


# test for approve_loan function
def test_approve_loan():
    # Test if approve_immediately returns True
    assert approve_loan(loan_amount=10000, credit_score=800, yearly_income=100000, has_cosigner=True) == True

    # Test if approve_based_on_ratio returns True
    assert approve_loan(loan_amount=10000, credit_score=700, yearly_income=70000, has_cosigner=False) == True

    # Test if all conditions fail
    assert approve_loan(loan_amount=10000, credit_score=600, yearly_income=50000, has_cosigner=False) == False
