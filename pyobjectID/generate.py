import time
import random
from bson import ObjectId


def generate() -> ObjectId:
    """
    Generate a new MongoDB ObjectId.

    This function creates a new ObjectId by combining a timestamp,
    a randomly generated machine ID, process ID, and a counter.
    The generated ObjectId is unique and can be used for identifying
    documents in a MongoDB database.

    Returns:
        ObjectId: A new MongoDB ObjectId generated from the
        current timestamp and random values.
    """
    # Generate a timestamp (4 bytes)
    timestamp = int(time.time())

    # Generate a random machine ID (24 bits)
    machine_id = random.getrandbits(24)

    # Generate a random process ID (16 bits)
    process_id = random.getrandbits(16)

    # Generate a random counter (24 bits)
    counter = random.getrandbits(24)

    # Combine components into a hexadecimal string
    generated_id = (
        f"{timestamp:08x}"
        f"{machine_id:06x}"
        f"{process_id:04x}"
        f"{counter:06x}"
    )

    return ObjectId(generated_id)
