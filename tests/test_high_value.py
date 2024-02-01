from lib.high_value import *

def test_first_value_given_is_higher():
    value_given = HighValue(10, 5)
    assert value_given.get_highest() == "First value is higher"
    
def test_second_value_given_is_higher():
    value_given = HighValue(5, 10)
    assert value_given.get_highest() == "Second value is higher"

def test_both_values_given_are_equal():
    value_given = HighValue(5, 5)
    assert value_given.get_highest() == "Values are equal"

def test_value_is_increased_using_first_selection_and_highest_checked():
    value_given = HighValue(5, 5)
    value_given.add(4, "first")
    assert value_given.get_highest() == "First value is higher"

def test_value_is_increased_using_second_selection_and_highest_checked():
    value_given = HighValue(5, 5)
    value_given.add(4, "second")
    assert value_given.get_highest() == "Second value is higher"