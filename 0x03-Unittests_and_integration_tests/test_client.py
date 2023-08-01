#!/usr//bin/env python3
"""test module for client.py"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for githuborgclient class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.GithubOrgClient')
    def test_org(self, org_name, mocked_github_org_client):
        mocked_github_org_client(org_name)
        mocked_github_org_client.return_value.org.return_value = False
        mocked_github_org_client.assert_called_once_with(org_name)
