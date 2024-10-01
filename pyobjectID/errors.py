from typing import Union
from bson import ObjectId


class InvalidObjectIdError(Exception):
    """
    Exception raised for invalid ObjectId values.

    This exception is thrown when a value that does not conform to
    the expected MongoDB ObjectId format is encountered.

    Attributes:
        object_id (Union[str, ObjectId]): The invalid ObjectId value
         that triggered the exception.
        message (str): An error message describing the reason for the
         exception (default is "Invalid ObjectId").
    """

    def __init__(self, object_id: Union[str, ObjectId], message: str = "Invalid ObjectId"):
        """
        Initialize the InvalidObjectIdError with a specific ObjectId
        and an optional message.

        Args:
            object_id (Union[str, ObjectId]): The invalid ObjectId
            that caused the exception.
            message (str, optional): Custom error message (default
            is "Invalid ObjectId").
        """
        if isinstance(object_id, ObjectId):
            object_id = str(object_id)
        self.object_id = object_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns:
            str: A string that includes the error message and the
            invalid ObjectId value.
        """
        return f'{self.message}: {self.object_id}'
