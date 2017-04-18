from unittest import TestCase

import datatypes

class TestData_type(TestCase):
    def test_none_type(self):
        self.assertEqual('no value', datatypes.data_type(None))

    def test_array_type(self):
        self.assertEqual(3, datatypes.data_type([1, 2, 3]))

    def test_small_array_type(self):
        self.assertEqual(None, datatypes.data_type([1, 2]))

    def test_small_booleans_type(self):
        self.assertEqual(True, datatypes.data_type(True))

    def test_small_integer_type(self):
        self.assertEqual('less than 100', datatypes.data_type(3))

    def test_large_integer_type(self):
        self.assertEqual('more than 100', datatypes.data_type(200))

    def test_str_type(self):
        self.assertEqual(6, datatypes.data_type('andela'))
