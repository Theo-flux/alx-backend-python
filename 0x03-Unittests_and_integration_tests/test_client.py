#!/usr/bin/env python3
"""test module for client.py"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from typing import Dict

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for githuborgclient class"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login', 'abc'})
    ])
    @patch('client.get_json')
    def test_org(
        self,
        org_name: str,
        out: Dict,
        mocked_get_json
    ) -> None:
        """
        test case for client.githubClientOrg.org() method

        Args:
            org_name (str): _description_
            out (Dict): _description_
            mocked_get_json (MagicMock): _description_
        """
        mocked_get_json.return_value = MagicMock()
        mocked_get_json.return_value.return_value = out
        test_github_org_client = GithubOrgClient(org_name)
        self.assertEqual(test_github_org_client.org(), out)
        mocked_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    def test_public_repos_url(self) -> None:
        """test case for protected _public_repos_url"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:

            repo = {
                'login': 'google',
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            mock_org.return_value = repo

            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                repo['repos_url']
            )
