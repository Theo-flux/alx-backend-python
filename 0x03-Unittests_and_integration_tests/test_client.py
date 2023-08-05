#!/usr/bin/env python3
"""test module for client.py"""
import unittest
import requests
from requests import get, HTTPError
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), out)
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
        """
        test case for has_license method

        Args:
            repo (Dict): _description_
            license_key (str): _description_
            expected (bool): _description_
        """
        gh_client = GithubOrgClient('google')
        repo_license = gh_client.has_license(repo, license_key)
        self.assertEqual(repo_license, expected)


@parameterized_class(
    (
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos"
    ),
    [(
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3],
    )]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient

    Args:
        unittest (_type_): _description_
    """
    @classmethod
    def setUpClass(cls):

        def payload_url(url):
            if url == cls.org_payload or url == cls.repos_payload:
                return MagicMock(**{'json.return_value': url})
            return HTTPError

        get_patcher = patch('requests.get')
        get_patcher.side_effect = payload_url
        cls.patcher = get_patcher
        cls.patcher.start()

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """
        test case for public_repos

        Args:
            mocked_get_json (_type_): _description_
        """
        mocked_get_json.return_value = repos_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mocked_public_url:
            mocked_public_url._public_repos_url = org_payload
            self.assertEqual(
                GithubOrgClient('google').public_repos(),
                expected_repos
            )

    @patch('client.get_json')
    def test_public_repos_with_license(self, license_key="apache-2.0") -> None:
        """
        test case for public_repos with license key

        Args:
            license_key (str): _description_
        """
        mocked_get_json.return_value = repos_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mocked_public_url:
            mocked_public_url._public_repos_url = org_payload
            self.assertEqual(
                GithubOrgClient('google').public_repos(license_key),
                apache2_repos
            )

    @classmethod
    def tearDownClass(cls):
        cls.patcher.stop()
