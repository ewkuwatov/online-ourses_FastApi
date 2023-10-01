from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str
    price: str


class EditCourse(BaseModel):
    new_name: str
    new_description: str
    new_price: str
    course_id: int