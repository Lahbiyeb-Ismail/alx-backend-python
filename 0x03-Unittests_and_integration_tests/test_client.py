#!/usr/bin/env python3
"""
Class contains unit tests.
"""

from unittest import TestCase
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class
from requests import HTTPError

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
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        }
    ]
)
class TestIntegrationGithubOrgClient(TestCase):
    """
    This class represents the test cases for the GithubOrgClient integration.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the test class before running any test cases.
        """
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test case for the public_repos method of the GithubOrgClient class.
        """

        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public repos with License"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])

        test = test_class.public_repos("apache-2.0")
        self.assertEqual(test, self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()
