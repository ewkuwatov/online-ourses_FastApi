from fastapi import APIRouter

from category import CourseCategory, EditCourseCategory

from database.categoryservice import add_category_db, edit_category_db, delete_categoryt_db, get_all_category_db

category_router = APIRouter(prefix='/category', tags=['Работа с категориями'])

@category_router.post('/public_category')
async def public_category(data: CourseCategory):
    result = add_category_db(**data.model_dump())

    return {'status': 1, 'message': result}

@category_router.put('/change_category')
async def change_category(data: EditCourseCategory):
    result = edit_category_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Категория не найден'}

@category_router.delete('/delete_category')
async def delete_category(category_id: int):
    result = delete_categoryt_db(category_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Категория не найден'}

@category_router.get('/get_all_category')
async def get_all_category():
    result = get_all_category_db()

    return {'status': 1, 'message': result}


