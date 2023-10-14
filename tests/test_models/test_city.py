#!/usr/bin/python3
""" Unit test City """

from datetime import datetime
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Unit tests for City class.
    """

    def test_initialization(self):
        """
        Test initialization of City class.
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict_method(self):
        """
        Test the to_dict() method in City.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', city_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(city_dict['__class__'], 'City', "__class__ key should have correct class name")
        self.assertIn('created_at', city_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', city_dict, "Dictionary should contain 'updated_at' key")

if __name__ == '__main__':
    unittest.main()
