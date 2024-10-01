import unittest

from bson import ObjectId

from pyobjectID.errors import InvalidObjectIdError

from pyobjectID import PyObjectId


class TestStringToObject(unittest.TestCase):
    """Test the to_object function in the PyObjectId module"""
    def test_string_to_object(self):
        obj = PyObjectId.to_object("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertIsInstance(obj, ObjectId, "String should be converted to an object")

    def test_string_to_object_type(self):
        obj = PyObjectId.to_object("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertEqual(obj, ObjectId("60f3d3f0b5c4b1d5d9a4e4c3"), "String should be converted to an object")

    def test_string_to_object_length(self):
        obj = PyObjectId.to_object("60f3d3f0b5c4b1d5d9a4e4c3")
        self.assertEqual(len(str(obj)), 24, "String should be converted to an object")

    def test_invalid_object_id(self):
        with self.assertRaises(InvalidObjectIdError):
            PyObjectId.to_object("invalidObjectId")

    def test_invalid_object_id_message(self):
        with self.assertRaises(InvalidObjectIdError) as context:
            PyObjectId.to_object("invalidObjectId")
        self.assertEqual(str(context.exception), "Invalid ObjectId: invalidObjectId",
                         "Error message should include the invalid ObjectId value")