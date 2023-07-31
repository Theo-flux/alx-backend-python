#!/usr//bin/env python3
"""test module for client.py"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mocked_get_json: MagicMock):
        """test case for GithubOrgClient.org method"""
        test_gh_client = GithubOrgClient(org_name)

