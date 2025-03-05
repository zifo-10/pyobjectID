from bson import ObjectId
from typing import Any


from .errors import InvalidObjectIdError
from .validate import is_valid
from pydantic.json_schema import JsonSchemaMode


class PyObjectId:
    """
    A custom Pydantic field validator that handles MongoDB ObjectIds.

    This class enables seamless validation and conversion of ObjectId values
    in Pydantic models, ensuring that ObjectIds are correctly handled in
    both directions (to and from MongoDB).

    Typical use case:
        You can use `PyObjectId` in a Pydantic model to automatically validate
        and convert string inputs to MongoDB ObjectId objects.

    Example usage:
        from pydantic import BaseModel
        from pyobjectID import PyObjectId

        class UserModel(BaseModel):
            id: PyObjectId

        user = UserModel(id="507f1f77bcf86cd799439011")

    The above example will ensure that the `id` is validated as a valid ObjectId
    before it's assigned to the model.
    """

    @classmethod
    def __get_validators__(cls):
        """
        Return the Pydantic validators for this field.

        This method is called by Pydantic to retrieve the sequence of
        validation methods. It yields the `to_object` method, which is responsible
        for validating and converting input values to MongoDB ObjectIds.

        Yields:
            A callable that performs the ObjectId conversion.
        """
        yield cls.to_object

    @classmethod
    def to_object(cls, value: Any, *args, **kwargs) -> 'PyObjectId':
        """
        Validate and convert a given value into a MongoDB ObjectId.

        If the input value is already an instance of `ObjectId`, it is returned
        as-is. Otherwise, the function attempts to convert a valid string
        representation into an `ObjectId`.

        Args:
            value (Any): The input value to validate and convert. This can be
            a string (typically the hexadecimal representation of an ObjectId)
            or an existing `ObjectId` instance.

        Returns:
            ObjectId: A valid MongoDB `ObjectId` object.

        Raises:
            InvalidObjectIdError: Raised if the input is not a valid ObjectId
            or cannot be converted to one.
        """
        if isinstance(value, ObjectId):
            return value
        try:
            if is_valid(value):
                return ObjectId(value)
            raise InvalidObjectIdError(value)
        except Exception:
            raise InvalidObjectIdError(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: JsonSchemaMode, *args) -> dict:
        """
        Define the custom JSON schema for PyObjectId.

        This method returns a schema that tells Pydantic how to represent the
        `PyObjectId` field in JSON schema outputs. It marks the field as a string
        in JSON, with the format type `objectid`, allowing for more accurate
        schema generation.

        Args:
            schema (JsonSchemaMode): The current schema mode for Pydantic.

        Returns:
            dict: A dictionary defining the JSON schema for `PyObjectId`.
        """
        return {
            "type": "string",
            "format": "objectid",
            "example": "507f1f77bcf86cd799439011",
        }
