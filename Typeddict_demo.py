from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_person:person={'name':'dimpal','age':'22'}
print(new_person)