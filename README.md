# Dataclass to Pydantic Conversion

To convert a data class to a Pydantic model, you can use the `pydantic.dataclasses.dataclass` decorator provided by Pydantic. This decorator allows you to define a Pydantic model using the syntax of Python's built-in `dataclass` decorator.

## Installation

You can install Pydantic using pip:

```pip install pydantic```

## Usage

### Import the necessary modules:

```python
from dataclasses import dataclass
from pydantic.dataclasses import dataclass as pydantic_dataclass
```

### Define your data class using the dataclass decorator:

```python
@dataclass
class Person:
    name: str
    age: int
```

### Convert the data class to a Pydantic model using the pydantic_dataclass decorator:

```python
PydanticPerson = pydantic_dataclass(Person)
```

### Now, PydanticPerson is a Pydantic model that behaves similarly to the original data class. You can use it for validation, serialization, and other Pydantic features.

For example, you can create an instance of PydanticPerson, validate it, and access its attributes:

```python
person = PydanticPerson(name="Amandeep", age=27)
person_dict = person.__dict__
print(person_dict)
# {'name': 'Amandeep', 'age': 27, '__pydantic_initialised__': True}
```

### You can also define additional validation rules, default values, and other Pydantic-specific features in the original data class, and they will be preserved in the converted Pydantic model.

### For more information, refer to the [Pydantic documentation](https://docs.pydantic.dev/latest/).


