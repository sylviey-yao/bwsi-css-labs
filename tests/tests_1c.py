"""
tests_1c.py

This module contains unit tests for the maximum sum of a subarray
"""

import pytest

from labs.lab_1.lab_1c import max_subarray_sum

def test_subarray_sum():
    assert max_subarray_sum([]) == 0                   # Test for empty list
    assert max_subarray_sum([5,10,12,10]) == 37        # Test for the whole list addition
    assert max_subarray_sum([1]) == 1                  # Test for one value
    assert max_subarray_sum([-12, 3, 7]) == 10         # Test for addition with two negatives


if __name__ == "__main__":
    pytest.main()
