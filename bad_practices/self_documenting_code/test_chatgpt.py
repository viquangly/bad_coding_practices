
import pytest

from bad_practices.self_documenting_code import best


# Tests for the approve_immediately function
def test_approve_immediately_with_cosigner():
    assert best.approve_immediately(500, 1.5, True) == True


def test_approve_immediately_with_excellent_credit_score():
    assert best.approve_immediately(800, 1.0, False) == True


def test_approve_immediately_with_excellent_income_amount_ratio():
    assert best.approve_immediately(700, 2.0, False) == True


def test_approve_immediately_with_poor_qualifications():
    assert best.approve_immediately(400, 0.5, False) == False


# Tests for the approve_based_on_ratio function
def test_approve_based_on_ratio_with_good_credit_score_and_good_ratio():
    assert best.approve_based_on_ratio(700, 1.5) == True


def test_approve_based_on_ratio_with_good_credit_score_and_poor_ratio():
    assert best.approve_based_on_ratio(700, 0.5) == False


def test_approve_based_on_ratio_with_excellent_credit_score():
    with pytest.raises(ValueError):
        best.approve_based_on_ratio(800, 1.0)


# Tests for the approve_loan function
def test_approve_loan_with_immediate_approval():
    assert best.approve_loan(10000, 700, 20000, True) == True


def test_approve_loan_with_based_on_ratio_approval():
    assert best.approve_loan(15000, 650, 30000, False) == True


def test_approve_loan_with_no_approval():
    assert best.approve_loan(20000, 500, 40000, False) == False
