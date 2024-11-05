#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
