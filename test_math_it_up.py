import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(100)
  assert math_it_up.is_even(7) == False #passes in a trick odd number
  assert not math_it_up.is_even(51) #passes in a trick odd number
  assert math_it_up.is_even(0)
  assert math_it_up.is_even(-2)


def test_is_odd():
  assert math_it_up.is_odd(127)
  assert not math_it_up.is_odd(10) #passes in a trick even number
  assert math_it_up.is_odd(59)
  assert math_it_up.is_odd(592) == False #passes in a trick even number
  assert math_it_up.is_odd(-7)

def test_mean():
  assert math_it_up.mean([3,3,3]) # == 3
  assert math_it_up.mean([25,100,50,50]) # == 56.25
  assert math_it_up.mean([127]) # == 127

def test_median():
  assert math_it_up.median([9,3,7]) # == 7
  assert math_it_up.median([238013132,32,584,237183,1]) # == 584
  assert math_it_up.median([0,7382,0,8293,0,73493290,17]) # == 17
  assert math_it_up.median([1,3]) # == 2

def test_mode():
  assert math_it_up.mode([0,9203921,0,832913871,0,0,1,73823,17]) # == 0
  assert math_it_up.mode([2,4,2,4]) # == 2,4
  assert math_it_up.mode([9,8,0,576]) # == all of them