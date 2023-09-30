from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel

from database.userservice import login_user_db, register_user_db


user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])

@user_router.post('/login')
async def login_user(data: LoginUserModel):
    result = login_user_db(**data.model_dump())

    return {'status': 1, 'message': result}

@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    result = register_user_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователь с такой почтой уже есть'}

@user_router.put('/change_info')
async def change_info(data: EditUserModel):
    pass

