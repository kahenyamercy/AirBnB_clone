#!/usr/bin/python3
"""
This script contains unittests for the FileStorage class
"""

import unittest
from models import storage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """
        Set up testing environment
        """
        # Create a new instance of BaseModel for testing
        self.obj = BaseModel()
        self.obj.save()

    def test_all_method(self):
        """
        Test the all() method of FileStorage
        """
        # Test the all() method
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIn(f"{self.obj.__class__.__name__}.{self.obj.id}", objs)

    def test_new_method(self):
        """
        Test the new() method of FileStorage
        """
        # Test the new() method
        objs = storage.all()
        self.assertIn(f"{self.obj.__class__.__name__}.{self.obj.id}", objs)
        new_obj = BaseModel()
        storage.new(new_obj.to_dict())
        self.assertIn(f"{new_obj.__class__.__name__}.{new_obj.id}", storage.all())

    def test_save_and_reload_methods(self):
        """
        Test the save() and reload() methods of FileStorage
        """
        # Test the save() and reload() methods
        objs_before = storage.all()
        storage.save()
        storage.reload()
        objs_after = storage.all()
        self.assertEqual(objs_before, objs_after)

    def tearDown(self):
        """
        Clean up testing environment
        """
        # Clean up - remove the created instance
        del self.obj

if __name__ == '__main__':
    unittest.main()
