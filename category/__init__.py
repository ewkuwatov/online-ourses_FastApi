from pydantic import BaseModel

# Пример модели данных для категории курса
class CourseCategory(BaseModel):
    id: int
    name: str

class EditCourseCategory(BaseModel):
    new_name: str
    category_id: int


