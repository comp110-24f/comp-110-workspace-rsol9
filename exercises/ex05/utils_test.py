"""define unit tests for them"""

__author__ = "730771611"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(<list_object>, <index_to_insert_num>, <value_to_add>) 
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num> 
        # that is greater than the length of our <list_object>




def test_only_evens_using_empty_list(self):
    self.assertEqual(only_evens([]), [])


def test_only_evens_using_only_evens(self):
    self.assertEqual(only_evens([2, 4, 6]), [2, 4, 6])


def test_only_events_using_only_odds(self):
    self.assertEqual(only_evens([1, 3, 5]), [])








def test_sub_with_index_below_zero_and_above_length_of_list(self):
    self.assertEqual(sub([1, 2, 3, 4], -1, 10), [1, 2, 3, 4])


def test_sub_with_empty_list(self):
    self.assertEqual(sub([], 1, 5), [])


def test_sub_with_normal_values(self):
    self.assertEqual(sub([1, 2, 3, 4, 5, 6], 1, 5), [2, 3, 4, 5, 6])


def test_add_at_index_with_normal_values(self):
    lst = [1, 2, 3, 4]
    add_at_index(lst, 4, 3)
    self.assertEqual(lst, [1, 2, 3, 4, 4])


def test_add_at_index_with_at_list_end(self):
    lst = [1, 2, 3, 4]
    add_at_index(lst, 5, 4)
    self.assertEqual(lst, [1, 2, 3, 4, 5])


def test_add_at_index_with_error(self):
    lst = [1, 2, 3]
    add_at_index(lst, 4, 5)
    self.assertRaises(IndexError)
