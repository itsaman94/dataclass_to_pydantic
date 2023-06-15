from dataclasses import dataclass
from pydantic.dataclasses import dataclass as pydantic_dataclass

@dataclass
class Person:
    name: str
    age: int

PydanticPerson = pydantic_dataclass(Person)

person = PydanticPerson(name="Amandeep", age=27)
person_dict = person.__dict__
print(person_dict)
# {'name': 'Amandeep', 'age': 27, '__pydantic_initialised__': True}
