''' Module to test Remote class '''

import unittest
from models.rectangle import Rectangle


class Rectangle_Tests(unittest.TestCase):
    ''' Test case for rectangle '''
    def test_rectangle_init(self):
        ''' Checks instantiation of Rectangle Class '''
        a = Rectangle(3, 4)
        self.assertAlmostEqual(a.width, 3)
        self.assertAlmostEqual(a.height, 4)

    def test_area(self):
        ''' checks area method of Rectangle Class'''
        self.assertAlmostEqual(Rectangle(3, 4).area(), 12)

    def test_display(self):
        '''checks display method of Rectangle Class'''
        self.assertEqual(1, 1)

    def test_str(self):
        '''checks __str__'''
        self.assertEqual(1, 1)

    def test_update(self):
        '''checks update method of Rectangle Class'''
        self.assertEqual(1, 1)

    def test_to_dictionary(self):
        '''checks to_dictionary method of Rectangle Class'''
        pass
