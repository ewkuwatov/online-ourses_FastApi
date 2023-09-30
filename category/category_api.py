from fastapi import APIRouter

from category import CourseCategory, EditCourseCategory


category_router = APIRouter(prefix='/category', tags=['Работа с категориями'])

@category_router.post('/public_category')
async def public_category(data: CourseCategory):
    pass

@category_router.put('/change_category')
async def change_category(data: EditCourseCategory):
    pass

@category_router.delete('/delete_category')
async def delete_category(category_id: int):
    pass


