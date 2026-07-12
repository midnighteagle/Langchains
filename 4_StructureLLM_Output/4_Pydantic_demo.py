from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name : str = 'nitish'
    age : Optional[int] = None
    email: EmailStr
    cgpa:float = Field(gt = 0, lt = 10, default=5, description= 'A decimal value representing the cgpa of the student')
    
new_Student = {'age': '32', 'email':'abc@gmail.com',} #if you make int as string it is better smart that get it as int.
# new_Student = {'age': '32', 'email':'abc@gmail.com','cgpa':6} #if you make int as string it is better smart that get it as int.
# new_Student = {'age': 32}
# new_Student = {"name": 'Akshat'}

# new_Student:Student = {"name": 'Akshat'}
# new_Student1:Student = {}

Student = Student(**new_Student)

# converting the student in the Dictionary.
Student_dict = dict(Student)
# now by the help of Dict print the age of Student.
print(Student_dict['age'])

student_json = Student.model_dump_json()
print(student_json)
print(student_json)
print(type(Student))
print(Student)
print(Student)