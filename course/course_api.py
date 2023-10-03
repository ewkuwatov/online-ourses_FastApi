from fastapi import APIRouter

from course import Course, EditCourse, EditCourseCategory

from database.courseservice import add_course_db, edit_course_db, edit_course_category_db, delete_course_db, get_all_course_db

course_router = APIRouter(prefix='/course', tags=['Работа с курсом'])

@course_router.post('/public_course')
async def public_course(data: Course):
    result = add_course_db(**data.model_dump())

    return {'status': 1, 'message': result}


@course_router.put('/change_course')
async def change_course(data: EditCourse):
    result = edit_course_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Курс не найден'}

@course_router.put('/change_course_category')
async def change_course_category(data: EditCourseCategory):
    result = edit_course_category_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Курс не найден'}

@course_router.delete('/delete_course')
async def delete_course(course_name: str):
    result = delete_course_db(course_name)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Курс не найден'}

@course_router.get('/get_all_category')
async def get_all_category():
    result = get_all_course_db()

    return {'status': 1, 'message': result}


