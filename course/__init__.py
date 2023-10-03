from pydantic import BaseModel

class Course(BaseModel):
    name: str
    price: str
    category: str

class EditCourse(BaseModel):
    name: str
    new_name: str
    new_price: str

class EditCourseCategory(BaseModel):
    name: str
    new_category: str