import unittest
from pyobjectID.errors import InvalidObjectIdError
from pyobjectID import MongoObjectId

class TestObjectToString(unittest.TestCase):
    """Test the to_string function in the MongoObjectId module"""
    def test_object_to_string(self):
        obj = MongoObjectId.to_string("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertIsInstance(obj, str, "Object should be converted to a string")

    def test_object_to_string_type(self):
        obj = MongoObjectId.to_string("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertEqual(obj, "60f3d3f0b5c4b1d5d9a4e4c3", "Object should be converted to a string")

    def test_object_to_string_length(self):
        obj = MongoObjectId.to_string("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertEqual(len(obj), 24, "Object should be converted to a string")

    def test_invalid_object_id(self):
        with self.assertRaises(InvalidObjectIdError):
            MongoObjectId.to_string("invalidObjectId")

    def test_invalid_object_id_type(self):
        with self.assertRaises(InvalidObjectIdError):
            MongoObjectId.to_string("invalidObjectId")

    def test_invalid_object_id_message(self):
        with self.assertRaises(InvalidObjectIdError) as context:
            MongoObjectId.to_string("invalidObjectId")
        self.assertEqual(str(context.exception), "Invalid ObjectId: invalidObjectId",
                         "Error message should include the invalid ObjectId value")
