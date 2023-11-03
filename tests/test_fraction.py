import sys
import unittest
from pathlib import Path
import pytest
# Get the directory of the current file (test_fraction.py)
current_file_path = Path(__file__).resolve()

# Get the parent directory of the current file, which should be 'tests'
tests_dir = current_file_path.parent

# Get the project directory by going up one level from the 'tests' directory
project_dir = tests_dir.parent

# Add the 'src' directory to the sys.path
# The 'src' directory is a sibling of the 'tests' directory in your project structure
sys.path.append(str(project_dir / 'src'))

# Now you can import your Fraction class
from cs132_HW1 import Fraction

def test_get_num():
    x = Fraction(1, 2)
    assert x.get_num() == 1

def test_get_den():
    y = Fraction(2, 3)
    assert y.get_den() == 3

def test_fraction_simplification():
    z = Fraction(3, 6)
    assert str(z) == '1/2'

def test_subtraction():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x - y
    assert z == Fraction(-1, 6)

def test_multiplication():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x * y
    assert z == Fraction(1, 3)

def test_division():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x / y
    assert z == Fraction(3, 4)

def test_greater_than():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    assert not (x > y)

def test_radd():
    x = Fraction(1, 2)
    assert (1 + x) == Fraction(3, 2)

def test_iadd():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    x += y
    assert x == Fraction(7, 6)


if __name__ == '__main__':
    unittest.main()
