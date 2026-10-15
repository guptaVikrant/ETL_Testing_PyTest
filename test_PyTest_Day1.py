import pytest
import pytest_check as check
#from pip._internal.commands import check


def add(a, b):
    return a + b


def test_addition():
    c=add(10, 15)
    assert c == 30, "add method not correct"


def test_subtraction():
    assert 20 - 10 == 30,  "subtraction failed"

def test_compare_two_number_hard_assertion():
    print("Test started.....")
    num1 = 10
    num2 = 20
    assert num1 < num2, "num1 is not lesser than num2"
    assert num1 == num2, "Two numbers are not equal"
    assert num1 != 10, "Two numbers are equal"
    print("Test completed...")

def test_compare_twoNumbers_soft_assertion():

    check.is_false(30 == 30, "not false")
    check.is_true(20 - 10 > 30, "Two numbers again are not equal")
    check.equal( 101, 202, "add method not correct")