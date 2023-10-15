#!/usr/bin/python3
"""place class unittest"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Unit tests for Place class.
    """

    def test_to_dict_method(self):
        """
        Test the to_dict() method in Place.
        """
        place = Place()
        place.state_id = ""
        place.user_id = ""
        place.name = ""
        place.description = ""
        place.number_rooms = 0
        place.number_bathrooms = 0
        place.max_guest = 0
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = []
        
        place_dict = place.to_dict()
        
        self.assertIsInstance(place_dict, dict, "to_dict() should return a dictionary")
        self.assertIn('__class__', place_dict, "Dictionary should contain '__class__' key")
        self.assertEqual(place_dict['__class__'], 'Place', "__class__ key should have correct class name")
        self.assertIn('created_at', place_dict, "Dictionary should contain 'created_at' key")
        self.assertIn('updated_at', place_dict, "Dictionary should contain 'updated_at' key")
        self.assertIn('state_id', place_dict, "Dictionary should contain 'state_id' key")
        self.assertIn('user_id', place_dict, "Dictionary should contain 'user_id' key")
        self.assertIn('name', place_dict, "Dictionary should contain 'name' key")
        self.assertIn('description', place_dict, "Dictionary should contain 'description' key")
        self.assertIn('number_rooms', place_dict, "Dictionary should contain 'number_rooms' key")
        self.assertIn('number_bathrooms', place_dict, "Dictionary should contain 'number_bathrooms' key")
        self.assertIn('max_guest', place_dict, "Dictionary should contain 'max_guest' key")
        self.assertIn('price_by_night', place_dict, "Dictionary should contain 'price_by_night' key")
        self.assertIn('latitude', place_dict, "Dictionary should contain 'latitude' key")
        self.assertIn('longitude', place_dict, "Dictionary should contain 'longitude' key")
        self.assertIn('amenity_ids', place_dict, "Dictionary should contain 'amenity_ids' key")

    def test_initialization(self):
        """
        Test initialization of Place class.
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.state_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
