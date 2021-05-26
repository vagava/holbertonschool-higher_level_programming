#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' Class to test the module "6-max_integer"'''
    def test_list(self):
        ''' list requirements test '''
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_max(self):
        ''' return the max integer in a list '''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-3, -18, -5]), -3)
        self.assertAlmostEqual(max_integer([1]), 1)
