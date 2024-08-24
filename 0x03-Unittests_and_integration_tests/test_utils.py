#!/usr/bin/env python3
"""
Class contains unit tests.
"""

from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


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


class TestGetJson(TestCase):
    """
    This class contains unit tests for the `get_json` function
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """
        Test the get_json function.

        Args:
          test_url (str): The URL to test.
          test_payload (dict): The expected payload.

        Returns:
          None
        """
        config = {"return_value.json.return_value": test_payload}
        patcher = patch("requests.get", **config)

        mock = patcher.start()

        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()

        patcher.stop()


class TestMemoize(TestCase):
    """
    This class contains unit tests for the `memoize` function
    """

    def test_memoize(self):
        """
        Test the memoize decorator.

        This method tests the functionality of the memoize
        decorator by creating a TestClass
        with a method and a memoized property. The method
        returns the value 42, and the
        property calls the method. The test verifies that the
        method is only called once
        when accessing the property multiple times.

        Args:
          self: The instance of the test class.

        Returns:
          None
        """

        class TestClass:
            """Test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
