from fastapi import APIRouter

from course import Course, EditCourse

course_router = APIRouter(prefix='/course', tags=['Работа с курсами'])

@course_router.post('/public_course')
async def public_course(data: Course):
    pass

@course_router.put('/change_course')
async def change_course(data: EditCourse):
    pass

@course_router.delete('/delete_course')
async def delete_course(course_id: int):
    pass


