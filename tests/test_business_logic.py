import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from src.domain.business_logic_example import BusinessLogicExample

def test_business_logic_gte_ten_and_true():
    response = BusinessLogicExample.process(number=10, bool=True)
    expected_response = "The number is greater than or equal 10 and bool is True"

    assert expected_response == response


def test_business_logic_gte_ten_and_false():
    response = BusinessLogicExample.process(number=10, bool=False)
    expected_response = "The number is greater than or equal 10 and bool is False"

    assert expected_response == response


def test_business_logic_lte_ten_and_true():
    response = BusinessLogicExample.process(number=5, bool=True)
    expected_response = "The number is less than 10 and bool is True"

    assert expected_response == response


def test_business_logic_lte_ten_and_false():
    response = BusinessLogicExample.process(number=5, bool=False)
    expected_response = "The number is less than 10 and bool is False"

    assert expected_response == response
