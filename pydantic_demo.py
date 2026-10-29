from pydantic import BaseModel, EmailStr, Field
from typing import  Optional

class Student(BaseModel):
    name: str = 'dimpal'
    age: Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0,lt=10,default=5,description="CGPA must be between 0 and 10")

new_student = Student(name='dimpal', email='dimpal@example.com', cgpa=8.5)
print(new_student)
student = Student(**new_student.model_dump())

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()