#!/usr/bin/env python3
"""
python test file for utils module
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Tuple, Union, TypedDict, Dict

from utils import requests, access_nested_map, get_json


TypedTestPayload = TypedDict('TypedTestPayload', {'payload': bool})


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    # @parameterized.expand([
    #     ({}, ("a",), KeyError('a')),
    #     ({"a": 1}, ("a", "b"), KeyError('b')),
    # ])
    # def test_access_nested_map_exception(
    #     self,
    #     nested_map: Dict,
    #     path: Tuple[str],
    #     output: Union[int, Dict]
    # ) -> None:
        """
        test case for utils.get_json function

        Args:
            nested_map (Mapping): A paramterized nested map
            path (Sequence): A parameterized sqeuence of key
            output (Any): output value from tested function
        """
        # self.assertRaises(KeyError, access_nested_map, nested_map, path)


# class TestGetJson(unittest.TestCase):
#     """
#     Test suite for utils.get_json function
#     """
#     @parameterized.expand([
#         ("http://example.com", {"payload": True}),
#         ("http://holberton.io", {"payload": False})
#     ])
#     @patch.object(requests, 'get')
#     def test_get_json(
#         self,
#         test_url: str,
#         test_payload: TypedTestPayload,
#         mocked_requests_get
#     ):
#         """
#         test case for utils.get_json function

#         Args:
#             test_url (str): test url
#             test_payload TypedTestPayload: test payload
#             mocked_requests (_type_): mocked requests package
#         """
#         mocked_response = MagicMock(**{"json.return_value": test_payload})
#         mocked_requests_get.return_value = mocked_response

#         self.assertEqual(get_json(test_url), test_payload)
#         mocked_requests_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
