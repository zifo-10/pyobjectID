import unittest
from pyobjectID import validate

class TestValidateInput(unittest.TestCase):
    """Test the is_valid function in the validate module"""
    def test_valid_input(self):
        self.assertTrue(validate.is_valid("60f3d3f0b5c4b1d5d9a4e4c3"), "Valid input should return True")

    def test_invalid_input(self):
        self.assertFalse(validate.is_valid("invalidObjectId"), "Invalid input should return False")

    def test_valid_input_type(self):
        self.assertTrue(validate.is_valid("60f3d3f0b5c4b1d5d9a4e4c3"), "Valid input should return True")

    def test_invalid_input_type(self):
        self.assertFalse(validate.is_valid("invalidObjectId"), "Invalid input should return False")

