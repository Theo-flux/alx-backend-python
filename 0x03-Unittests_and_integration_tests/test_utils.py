#!/usr/bin/python3
"""
python test file for utils module
"""
import unittest
from unittest.mock import Mock, MagicMock
from parameterized import parameterized
from typing import Mapping, Sequence, Any

from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
