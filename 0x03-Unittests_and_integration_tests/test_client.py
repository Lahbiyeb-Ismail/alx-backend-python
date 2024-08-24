#!/usr/bin/env python3
"""
Class contains unit tests.
"""

from unittest import TestCase
from unittest.mock import PropertyMock, patch

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """
        Test case for the `public_repos` method of the `GithubOrgClient` class.

        Args:
          mock_json: A mock object for the `json` module.

        Returns:
          None

        Raises:
          AssertionError: If the result of the `public_repos`
          method does not match the expected result.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        client = "client.GithubOrgClient._public_repos_url"
        with patch(client, new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient("test")
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test the `has_license` method of the GithubOrgClient class.

        Args:
          repo (str): The name of the repository to check.
          license_key (str): The license key to search for.
          expected (bool): The expected result of the `has_license` method.

        Returns:
          None
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """
    This class represents the test cases for the GithubOrgClient integration.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class before running any test cases.

        This method is a class method and is called once before
        any test cases are executed.
        It is used to configure the necessary environment for the tests.

        Args:
          cls: The class object representing the test class.

        Returns:
          None
        """
        pass
        config = {
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload,
            ]
        }
        cls.get_patcher = patch("requests.get", **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test case for the public_repos method of the GithubOrgClient class.

        Returns:
          None
        """

        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()
