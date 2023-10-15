#!/usr/bin/python3
"""
Unittest for the Amenity class
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """

    def setUp(self):
        """
        Set up a test instance
        """
        self.amenity = Amenity()

    def test_instance_creation(self):
        """
        Test Amenity instance creation
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_attributes(self):
        """
        Test Amenity attributes
        """
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict_method(self):
        """
        Test the to_dict() method in Amenity.
        """
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', obj_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(obj_dict['__class__'], 'Amenity', "__class__ key should have correct class name")
        self.assertIn('created_at', obj_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', obj_dict, "Dictionary should contain 'updated_at' key")
        self.assertNotIn('name', obj_dict, "Dictionary should not contain 'name' key")

    def test_str_method(self):
        """
        Test Amenity __str__() method
        """
        string_representation = str(self.amenity)
        self.assertIsInstance(string_representation, str)
        self.assertIn("[Amenity]", string_representation)
        self.assertIn(self.amenity.id, string_representation)
        self.assertIn(self.amenity.name, string_representation)


if __name__ == '__main__':
    unittest.main()
