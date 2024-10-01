from bson import ObjectId
from typing import Any
from .errors import InvalidObjectIdError
from .validate import is_valid


class PyObjectId:
    """
    Custom validator for Pydantic that converts a user-friendly string
    representation into a MongoDB ObjectId.

    This validator is designed to ensure that input values conform to
    the MongoDB ObjectId format. It raises appropriate exceptions for
    invalid inputs, making it easier to work with ObjectIds in Pydantic
    models.

    Example usage:
        You can use this validator in a Pydantic model as follows:

        ```python
        from pydantic import BaseModel

        class UserModel(BaseModel):
            id: PyObjectId
        ```

    Attributes:
        None
    """

    @classmethod
    def __get_validators__(cls):
        """
        Get the validators for the PyObjectId class.

        Yields:
            Generator: A generator that yields the conversion method
            for validating input values as MongoDB ObjectIds.
        """
        yield cls.to_object

    @classmethod
    def to_object(cls, value: Any, *args, **kwargs) -> ObjectId:
        """
        Convert a given value into a MongoDB ObjectId.

        Args:
            value (Any): The value to be converted, which can be a
            string or an existing ObjectId.

        Returns:
            ObjectId: The converted ObjectId instance if the input is
            valid.

        Raises:
            InvalidObjectIdError: If the provided value is not a valid
            ObjectId or if the conversion fails.

        Example:
            >>> obj_id = PyObjectId.to_object("507f1f77bcf86cd799439011")
            >>> print(obj_id)
            ObjectId('507f1f77bcf86cd799439011')
        """
        if isinstance(value, ObjectId):
            return value
        try:
            if is_valid(value):
                return ObjectId(value)
            raise InvalidObjectIdError(value)
        except Exception:
            raise InvalidObjectIdError(value)
