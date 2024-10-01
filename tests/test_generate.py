import unittest

from bson import ObjectId

from pyobjectID import generate, is_valid, MongoObjectId
from pyobjectID.errors import InvalidObjectIdError

class TestGenerateModule(unittest.TestCase):
    """Test the generate function in the generate module"""
    def test_generate_object_id(self):
        new_id = generate()
        self.assertTrue(is_valid(new_id), "Generated ObjectId should be valid")

    def test_generate_object_id_type(self):
        new_id = generate()
        self.assertIsInstance(new_id, ObjectId, "Generated ObjectId should be of type ObjectId")

    def test_generate_object_id_not_string(self):
        new_id = generate()
        self.assertNotIsInstance(new_id, str, "Generated ObjectId should not be a string")

    def test_generate_object_id_length(self):
        new_id = generate()
        self.assertEqual(len(str(new_id)), 24, "Generated ObjectId should be 24 characters long")

    def test_generate_object_id_uniqueness(self):
        id1 = generate()
        id2 = generate()
        self.assertNotEqual(id1, id2, "Generated ObjectIds should be unique")

    def test_invalid_object_id(self):
        with self.assertRaises(InvalidObjectIdError):
            MongoObjectId.to_string("invalidObjectId")
