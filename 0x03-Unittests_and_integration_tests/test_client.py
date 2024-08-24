#!/usr/bin/env python3
"""
Class contains unit tests.
"""

from unittest import TestCase
from unittest.mock import PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Class for Testing Github Org Client"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, input, mock):
        """
        Test the org() method of the GithubOrgClient class.

        Args:
          input (str): The name of the organization.
          mock (MagicMock): The mock object used to assert the API call.

        Returns:
          None
        """
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{input}")

    def test_public_repos_url(self):
        """
        Test case for the `test_public_repos_url` method.

        This method tests the functionality of the
        `_public_repos_url` property in the `GithubOrgClient` class.
        It uses the `patch` function from the `unittest.mock`
        module to mock the `org` property of the `GithubOrgClient` class.
        The `org` property is replaced with a `PropertyMock`
        object that returns a predefined payload dictionary.
        The `GithubOrgClient` class is then instantiated with
        a test organization name.
        The `_public_repos_url` property is accessed and the
        result is compared to the value of the "repos_url" key
        in the payload dictionary.
        The test passes if the result is equal to the
        payload's "repos_url" value.

        """
        path = "client.GithubOrgClient.org"
        with patch(path, new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient("test")
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
