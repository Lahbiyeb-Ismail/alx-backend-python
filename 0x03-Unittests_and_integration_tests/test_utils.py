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
