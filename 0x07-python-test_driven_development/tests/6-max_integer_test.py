#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 3, 9.4, 2]), 9.4)
        self.assertEqual(max_integer([1, 3, -94, 2]), 3)
        self.assertEqual(max_integer([9.4]), 9.4)
        self.assertEqual(max_integer([1]), 1)
        matrix = ['m','r','k']
        self.assertEqual(max_integer(matrix),'r')

    def test_values(self):
        self.assertRaises(TypeError, max_integer(), [1, 3, "hamid", 2])
