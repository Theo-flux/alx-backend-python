#!/usr/bin/env python3
"""python test file for utils module"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import (
    Tuple,
    Dict,
    Union,
    Dict
)
import utils
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """
    test suite for utils.access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        output: Union[int, Dict]
    ) -> None:
        """
        test case for utils.access_nested_map function

        Args:
            nested_map (dict): A parameterized nested map
            path (Tuple[str]): A parameterized sqeuence of key
            output (Union[int, Dict]): output value from tested function
        """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b')),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        output: Union[int, Dict]
    ) -> None:
        """
        test case for utils.get_json function

        Args:
            nested_map (Mapping): A paramterized nested map
            path (Sequence): A parameterized sqeuence of key
            output (Any): output value from tested function
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch.object(utils.requests, 'get')
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
        mocked_requests_get
    ):
        """
        test case for utils.get_json function

        Args:
            test_url (str): test url
            test_payload TypedTestPayload: test payload
            mocked_requests (_type_): mocked requests package
        """
        mocked_response = MagicMock(**{"json.return_value": test_payload})
        mocked_requests_get.return_value = mocked_response

        self.assertEqual(get_json(test_url), test_payload)
        mocked_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    test suite for utils.memoize function
    """
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked_a_method:
            mocked_a_method.return_value = lambda: 42
            my_object = TestClass()
            self.assertEqual(my_object.a_property(), 42)
            self.assertEqual(my_object.a_property(), 42)
            self.assertEqual(mocked_a_method.call_count, 1)
