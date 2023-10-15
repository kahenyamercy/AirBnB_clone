#!/usr/bin/python3
"""Test for user class"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """
    def test_attributes(self):
        """
        Test if User instance has the expected attributes with correct default values.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """
        Test if User class inherits from the BaseModel class.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of the User class.
        """
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

if __name__ == '__main__':
    unittest.main()
