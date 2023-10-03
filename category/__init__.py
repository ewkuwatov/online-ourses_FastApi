from pydantic import BaseModel

# Пример модели данных для категории курса
class CourseCategory(BaseModel):
    name: str

class EditCourseCategory(BaseModel):
    name: str
    new_name: str


