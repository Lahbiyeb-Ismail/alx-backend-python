#!/usr/bin/env python3
"""
Class contains unit tests for the `access_nested_map` function.
"""

from unittest import TestCase

from parameterized import parameterized

access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(TestCase):
    """
    This class contains unit tests for the `access_nested_map` function.

    Methods:
      - test_access_nested_map: Tests the `access_nested_map`
      function with different inputs.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, keys, expected):
        """
        Tests the `access_nested_map` function with different inputs.

        Test Cases:
        - Test accessing a nested map with a single key.
        - Test accessing a nested map with multiple keys.
        """
        result = access_nested_map(nested_map, keys)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, keys):
        """
        Test case to verify that accessing a nested map with
        invalid keys raises a KeyError.

        Args:
          nested_map (dict): The nested map to be accessed.
          keys (list): The list of keys to access the nested map.

        Raises:
          AssertionError: If the KeyError is not raised
          or if the raised KeyError does not match the
          expected KeyError.

        Returns:
          None
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, keys)
        self.assertEqual(f"KeyError('{keys[-1]}')", repr(e.exception))
