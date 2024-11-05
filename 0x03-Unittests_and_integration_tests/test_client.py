#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import (
        org_payload, repos_payload,
        expected_repos, apache2_repos)


# Unit tests for client.GithubOrgClient
class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )


# Unit tests for client.GithubOrgClient._public_repos_url property
class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @patch("client.GithubOrgClient.org", new_callable=property)
    def test_public_repos_url(self, mock_org: property) -> None:
        """Test _public_repos_url property returns the expected URL"""
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test/repos"
                }
        client = GithubOrgClient("test")
        self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test/repos"
                )


# Unit tests for client.GithubOrgClient.public_repos
class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @patch("client.get_json")
    @patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
            )
    def test_public_repos(
            self,
            mock_public_repos_url: PropertyMock,
            mock_get_json: Mock) -> None:
        """Test public_repos method returns the expected list of repos"""
        mock_public_repos_url.return_value =
        "https://api.github.com/orgs/test/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test/repos"
                )


# Unit tests for client.GithubOrgClient.has_license
class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self, repo: dict,
            license_key: str, expected: bool) -> None:
        """Test has_license returns the expected boolean"""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


# Integration tests for GithubOrgClient.public_repos
@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the test class with patched requests.get"""
        cls.get_patcher = patch(
                "requests.get",
                side_effect=cls.mocked_requests_get
                )
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the test class and stop patching requests.get"""
        cls.get_patcher.stop()

    def mocked_requests_get(self, url: str) -> dict:
        """Mock requests.get to return fixture data based on URL"""
        if "orgs" in url:
            return org_payload
        elif "repos" in url:
            return repos_payload
        return {}

    def test_public_repos(self) -> None:
        """Test public_repos method returns the expected list of repos"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)


# Integration tests for GithubOrgClient
@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the test class with patched requests.get"""
        cls.get_patcher = patch(
                "requests.get",
                side_effect=cls.mocked_requests_get
                )
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the test class and stop patching requests.get"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url: str):
        """Mock requests.get to return fixture data based on the URL"""
        if "orgs" in url:
            return MockResponse(org_payload)
        elif "repos" in url:
            return MockResponse(repos_payload)
        return MockResponse({})

    def test_public_repos(self) -> None:
        """
        Test that public_repos method returns the expected list of repos
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test that public_repos method returns the repos
        with specified license
        """
        client = GithubOrgClient("test")
        self.assertEqual(
                client.public_repos(license="apache-2.0"),
                self.apache2_repos
                )


class MockResponse:
    """Mock response class for requests.get"""

    def __init__(self, json_data: dict, status_code: int = 200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self) -> dict:
        """Return the JSON data"""
        return self.json_data
