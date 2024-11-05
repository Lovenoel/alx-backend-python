#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
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
