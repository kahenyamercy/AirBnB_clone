#!/usr/bin/python3
"""review unittest"""

import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    """
    Unit tests for Review class.
    """

    def test_review_attributes(self):
        """
        Test Review attributes initialization.
        """
        review = Review()
        self.assertEqual(review.place_id, "", "Default place_id should be an empty string")
        self.assertEqual(review.user_id, "", "Default user_id should be an empty string")
        self.assertEqual(review.text, "", "Default text should be an empty string")

    def test_to_dict_method(self):
        """
        Test the to_dict() method in Review.
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', review_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(review_dict['__class__'], 'Review', "__class__ key should have correct class name")
        self.assertIn('created_at', review_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', review_dict, "Dictionary should contain 'updated_at' key")
        # Check if place_id is absent
        self.assertNotIn('place_id', review_dict, "Dictionary should not contain 'place_id' key")
        # Check if user_id is absent
        self.assertNotIn('user_id', review_dict, "Dictionary should not contain 'user_id' key")

    def test_review_str_method(self):
        """
        Test the __str__() method in Review.
        """
        review = Review()
        string_representation = str(review)
        self.assertIsInstance(string_representation, str, "__str__() should return a string")
        self.assertIn("[Review]", string_representation, "String representation should contain '[Review]'")

if __name__ == '__main__':
    unittest.main()
