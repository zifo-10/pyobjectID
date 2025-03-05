from typing import Any
from .errors import InvalidObjectIdError
from pyobjectID.validate import is_valid
from bson import ObjectId
from pydantic.json_schema import JsonSchemaMode


class MongoObjectId:
    """
    A custom Pydantic validator to handle the conversion of MongoDB ObjectIds
    into their string representations.

    This class ensures that input values provided in Pydantic models are valid
    MongoDB ObjectIds or can be converted into a valid ObjectId string format.
    It raises `InvalidObjectIdError` for invalid inputs.

    Example usage:
        from pydantic import BaseModel
        from pyobjectID import MongoObjectId

        class DocumentModel(BaseModel):
            id: MongoObjectId

        doc = DocumentModel(id="507f1f77bcf86cd799439011")
    """

    @classmethod
    def __get_validators__(cls):
        """
        Yield the validator function(s) for Pydantic to use with MongoObjectId.

        Pydantic calls this method to get the validation method that will convert
        and validate MongoDB ObjectIds. It yields the `to_string` method, which
        ensures the value is either an ObjectId or a valid ObjectId string.

        Yields:
            Callable: The method responsible for validating and converting
            the input value into a string representation of an ObjectId.
        """
        yield cls.to_string

    @classmethod
    def to_string(cls, value: Any, *args, **kwargs) -> 'MongoObjectId':
        """
        Validate and convert a MongoDB ObjectId or string input into its string representation.

        This method ensures that the provided input is either a valid MongoDB ObjectId
        or a string that can be converted to one. If the input is valid, it returns the
        string representation of the ObjectId.

        Args:
            value (Any): The value to be validated and converted. It can be an
            ObjectId instance or a valid ObjectId string.

        Returns:
            str: The string representation of the ObjectId.

        Raises:
            InvalidObjectIdError: Raised when the provided value is not a valid
            ObjectId or cannot be converted to a valid ObjectId string.

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

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: JsonSchemaMode, *args) -> dict:
        """
        Define the custom JSON schema representation for MongoObjectId.

        This method provides a custom JSON schema that tells Pydantic how to
        represent `MongoObjectId` in its JSON schema output. The schema specifies
        that the field is a string with the format `objectid`, providing an example
        of a typical MongoDB ObjectId.

        Args:
            schema (JsonSchemaMode): The current schema mode for Pydantic.

        Returns:
            dict: A JSON schema dictionary that defines how `MongoObjectId`
            should be represented in schemas.
        """
        return {
            "type": "string",
            "format": "objectid",
            "example": "507f1f77bcf86cd799439011",
        }
