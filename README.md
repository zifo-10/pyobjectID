# PYOBJECTID

![PyPI](https://img.shields.io/pypi/v/pyobjectID)

`pyobjectID` is a Python package designed to simplify the generation, validation, and manipulation of MongoDB ObjectIds. Whether you're working with databases directly or integrating ObjectIds into your Pydantic models, this package provides a straightforward and efficient solution.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Operations](#basic-operations)
  - [Pydantic Integration](#pydantic-integration)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

## Features

- **Generate**: Create new MongoDB ObjectIds.
- **Validate**: Check the validity of existing ObjectIds.
- **Convert**: Easily convert between strings and ObjectIds.
- **Integration**: Seamless compatibility with Pydantic for data validation.

## Installation

You can install the package using pip:

```bash
pip install pyobjectid
```

## Installation from Source

To install from source, clone the repository and install the dependencies:
```
git clone https://github.com/yourusername/pyobjectID.git
cd pyobjectID
pip install .
```

## Usage
### Basic Operations

You can perform basic operations such as generating, validating, and converting ObjectIds:

```
from pyobjectID import (generate, PyObjectId, 
                        MongoObjectId, is_valid)

# Generate a new ObjectId
new_id = generate()
print(f"Generated ObjectId: {new_id}")

# Validate an ObjectId
valid = is_valid(new_id)
print(f"Is the ObjectId valid? {valid}")

# Convert a string to a PyObjectId
py_object_id = PyObjectId.to_object(new_id)
print(f"PyObjectId: {py_object_id}")

# Convert a PyObjectId to a string
mongo_object_id = MongoObjectId.to_string(py_object_id)
print(f"MongoObjectId: {mongo_object_id}")
```

### Pydantic Integration

This package can be used in Pydantic models to validate ObjectId fields from MongoDB. Here are examples of how to implement it:
```
from pydantic import BaseModel
from pyobjectID import PyObjectId, MongoObjectId

class User(BaseModel):
    id: PyObjectId  # Automatically validates and converts to ObjectId
    name: str
    email: str

class GetFromMongo(BaseModel):
    id: MongoObjectId  # Automatically validates and converts to string
```

- In the User model, the id field will be validated as a valid ObjectId, and any string assigned to it will be converted to an ObjectId.
- In the GetFromMongo model, the id field will be validated as a valid ObjectId and will be converted to a string.

## Running Tests

To run the unit tests for this project, use the following command:

```
python -m unittest discover -s test
```

## Contributing
Contributions are welcome! If you have suggestions or find bugs, please create an issue or submit a pull request.

