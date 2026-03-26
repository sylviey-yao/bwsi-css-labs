"""
tests_1d.py

This module contains unit tests for finding the indices that return the sum of a target number
"""

import pytest

from labs.lab_1.lab_1d import two_sum

def test_targetted_sum():
    assert two_sum([2, 3, 7, 10], 10) == [1, 2]             # Test for list with one of the values in it
    assert two_sum([5,-1, 3,], 4) == [0,1]                  # Test for the addition of a positive with a negativfe
    assert two_sum([1, 6, 12], 5) == []                     # Test for non existent value
    assert two_sum([-12, 3, 7], 10) == [1, 2]               # Test for addition of two numbers after a negative


if __name__ == "__main__":
    pytest.main()
