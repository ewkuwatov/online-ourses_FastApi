from pydantic import BaseModel

class Comment(BaseModel):
    user: str
    comment: str
    course: str

class EditComment(BaseModel):
    id: str
    new_comment: str
