#!/usr/bin/python3
"""unit testing"""
import unittest
from models.base_model import BaseModel
from datetime import timedelta, datetime

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for BaseModel class.
    """

    def test_instance_creation(self):
        """
        Test if a BaseModel instance is created with the expected attributes.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        obj = BaseModel()
        string_representation = str(obj)
        self.assertIsInstance(string_representation, str)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn(obj.id, string_representation)

    def setUp(self):
        """
        Set up a base model instance for testing.
        """
        self.base_model = BaseModel()

    def test_id_generation(self):
        """
        Test ID generation in BaseModel.
        """
        self.assertIsNotNone(self.base_model.id, "ID should be generated")
        self.assertEqual(len(self.base_model.id), 36, "ID should be a valid UUID")

    def test_created_at_and_updated_at(self):
        """
        Test initialization of created_at and updated_at attributes in BaseModel.
        """
        self.assertIsNotNone(self.base_model.created_at, "Created_at should be initialized")
        self.assertIsNotNone(self.base_model.updated_at, "Updated_at should be initialized")
        """ Define a tolerance level (e.g., 1 millisecond)"""
        tolerance = timedelta(milliseconds=1)

        # Check if the difference between created_at and updated_at is within the tolerance
        time_difference = abs(self.base_model.updated_at - self.base_model.created_at)
        self.assertLessEqual(time_difference, tolerance, "Created_at and Updated_at should be the same initially within the tolerance")

    def test_save_method(self):
        """
        Test the save() method in BaseModel.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at, "Updated_at should change after calling save()")

    def test_to_dict_method(self):
        """
        Test the to_dict() method in BaseModel.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', obj_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(obj_dict['__class__'], 'BaseModel', "__class__ key should have correct class name")
        self.assertIn('created_at', obj_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', obj_dict, "Dictionary should contain 'updated_at' key")

if __name__ == '__main__':
    unittest.main()
