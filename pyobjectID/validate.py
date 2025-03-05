import datetime
import re
import time

from bson import ObjectId


def is_valid(object_id: str | ObjectId) -> bool:
    """
    Validate if the given string is a valid MongoDB ObjectId.

    A valid ObjectId must be a 24-character hexadecimal string.
    This function also checks if the timestamp portion of the
    ObjectId is reasonable, ensuring it is not in the future
    and corresponds to a valid datetime.

    Args:
        object_id (str): The string representation of the ObjectId
        to validate.

    Returns:
        bool: True if the string is a valid ObjectId, False otherwise.

    Example:
        >>> is_valid("507f1f77bcf86cd799439011")
        True
        >>> is_valid("invalidObjectId")
        False
    """
    object_id = str(object_id)

    # Check if the length is 24 characters and contains only hexadecimal characters
    if not re.match(r'^[0-9a-f]{24}$', object_id):
        return False

    # Extract the timestamp (first 8 characters)
    timestamp_hex = object_id[:8]
    timestamp = int(timestamp_hex, 16)

    # Check if the timestamp is a reasonable date
    if timestamp < 0 or timestamp > int(time.time()):
        return False

    # Optional: Check if the timestamp corresponds to a valid datetime
    try:
        datetime.datetime.utcfromtimestamp(timestamp)
    except ValueError:
        return False

    return True
