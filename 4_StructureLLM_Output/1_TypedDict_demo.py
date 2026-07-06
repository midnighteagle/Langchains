from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_Person: Person = {'name': 'Nitish', 'age': 35}
new1_Person: Person = {'name': 'Nitish', 'age': '35'}

print(new_Person)
print(new1_Person)