from typing import Any
from .errors import InvalidObjectIdError
from pyobjectID.validate import is_valid
from bson import ObjectId


class MongoObjectId:
    """
    Custom validator for Pydantic to convert a MongoDB ObjectId
    to its string representation.

    This validator ensures that the input value is either a
    valid ObjectId or a string that can be converted to an
    ObjectId. If the value is invalid, it raises an
    InvalidObjectIdError.
    """

    @classmethod
    def __get_validators__(cls):
        """
        Get the validators for the MongoObjectId class.

        Yields:
            Generator: A generator that yields the conversion
            method for validating input values as MongoDB
            ObjectIds.
        """
        yield cls.to_string

    @classmethod
    def to_string(cls, value: Any, *args, **kwargs) -> str:
        """
        Convert a MongoDB ObjectId to its string representation.

        Args:
            value (Any): The value to be converted, which can be
            a MongoDB ObjectId or a string.

        Returns:
            str: The string representation of the MongoDB ObjectId.

        Raises:
            InvalidObjectIdError: If the provided value is not a
            valid ObjectId or cannot be converted.

        Example:
            >>> obj_id = MongoObjectId.to_string(ObjectId("507f1f77bcf86cd799439011"))
            >>> print(obj_id)
            '507f1f77bcf86cd799439011'
        """
        if isinstance(value, ObjectId):
            return str(value)

        if isinstance(value, str):
            if not is_valid(value):
                raise InvalidObjectIdError(value)
            return value

        raise InvalidObjectIdError(value)
