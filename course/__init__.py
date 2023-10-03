from pydantic import BaseModel

class Course(BaseModel):
    name: str
    discription: str
    video: str
    category: str

class EditCourse(BaseModel):
    name: str
    new_name: str
    new_discription: str
    new_video: str

class EditCourseCategory(BaseModel):
    name: str
    new_category: str