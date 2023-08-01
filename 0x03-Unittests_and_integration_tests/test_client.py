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

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """
        test case for public_repos

        Args:
            mocked_get_json (_type_): _description_
        """
        list_of_public_repos = [
            {'name': 'truth'},
            {'name': 'multi-servers'},
            {'name': 'ar'}
        ]
        mocked_get_json.return_value = list_of_public_repos

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mocked_public_url:
            org_res = {
                'login': 'google',
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            public_repos = ['truth', 'multi-servers', 'ar']

            mocked_public_url._public_repos_url = org_res['repos_url']
            self.assertEqual(
                GithubOrgClient('google').public_repos(),
                public_repos
            )
            self.assertEqual(mocked_public_url.call_count, 1)

        self.assertEqual(mocked_get_json.call_count, 1)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
        self,
        repo: Dict,
        license_key: str,
        expected: bool
    ) -> None:
        """test case for has_license method"""
        test_gh_license = GithubOrgClient('google')
        test_repo_license = test_gh_license.has_license(repo, license_key)
        self.assertIsNotNone(test_repo_license)
        self.assertEqual(test_repo_license, expected)
