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
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        client = "client.GithubOrgClient.org"
        with patch(client, new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient("test")
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
