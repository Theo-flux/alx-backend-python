#!/usr/bin/env python3
"""
python test file for utils module
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Mapping, Sequence, Any, TypedDict

from utils import access_nested_map, get_json


TypedTestPayload = TypedDict('TypedTestPayload', {'payload': bool})


class TestAccessNestedMap(unittest.TestCase):
    """
    test suite for utils.access_nested_map method

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        output: Any
    ):
        """
        test case for utils.access_nested_map method

        Args:
            nested_map (Mapping): A parametarzed nested map
            path (Sequence): A parametarzed sqeuence of key
            output (Any): output value from tested function
        """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b')),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        output: Any
    ):
        """
        test case for utils.get_json method

        Args:
            nested_map (Mapping): A parametarzed nested map
            path (Sequence): A parametarzed sqeuence of key
            output (Any): output value from tested function
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for utils.get_json method

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(
        self,
        test_url: str,
        test_payload: TypedTestPayload,
        mocked_requests
    ):
        """
        test case for utils.get_json

        Args:
            test_url (str): test url
            test_payload TypedTestPayload: test payload
            mocked_requests (_type_): mocked requests package
        """
        mocked_response = MagicMock()
        mocked_response.json.return_value = test_payload
        mocked_requests.get.return_value = mocked_response

        self.assertEqual(get_json(test_url), test_payload)
        mocked_requests.get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
