from fastapi import APIRouter

from comment import Comment, EditComment

from database.commentservice import add_comment_db, edit_comment_db, get_all_comment_db

comment_router = APIRouter(prefix='/comment', tags=['Работа с комментами'])

@comment_router.post('/public_comment')
async def public_category(data: Comment):
    result = add_comment_db(**data.model_dump())

    return {'status': 1, 'message': result}

@comment_router.put('/change_comment')
async def change_category(data: EditComment):
    result = edit_comment_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'коммент не найден'}


@comment_router.get('/get_all_category')
async def get_all_category():
    result = get_all_comment_db()

    return {'status': 1, 'message': result}


