#!/usr/bin/python3
"""Unit test for state class"""
import unittest
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):
    """
    Unit tests for State class.
    """

    def test_attributes(self):
        """
        Test attributes of State class.
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_to_dict_method(self):
        """
        Test the to_dict() method in State.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', state_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(state_dict['__class__'], 'State', "__class__ key should have correct class name")
        self.assertIn('created_at', state_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', state_dict, "Dictionary should contain 'updated_at' key")
        self.assertIn('id', state_dict, "Dictionary should contain 'id' key")
        self.assertNotIn('name', state_dict, "Dictionary should not contain 'name' key")

    def test_attribute_types(self):
        """
        Test types of attributes in State instance.
        """
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    def test_name_assignment(self):
        """
        Test if name is correctly assigned.
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California", "Name should be correctly assigned")

    def test_str_representation(self):
        """
        Test the __str__ representation of State.
        """
        state = State()
        state.name = "New York"
        str_representation = str(state)
        self.assertIn("[State] (", str_representation)
        self.assertIn("New York", str_representation)

if __name__ == '__main__':
    unittest.main()
