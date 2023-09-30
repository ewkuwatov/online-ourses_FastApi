from datetime import datetime

from database.models import User
from database import get_db


# Регистрация пользователя
def register_user_db(name, surname, email, phone_number, password):
    db = next(get_db())

    cheker = db.query(User).filter_by(email=email).first()

    if cheker:
        return False

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    password=password, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегистрирован'

# Вход в аккаунт
def login_user_db(email, password):
    db = next(get_db())

    cheker = db.query(User).filter_by(email=email).first()

    if cheker:
        if cheker.password == password:
            return cheker
        elif cheker.password != password:
            return 'Неверный пароль'

    return 'Ошибка в данных'

# Добавить фото профиля
def add_profile_photo_db(user_id, photo):
    db = next(get_db())

    cheker = db.query(User).filter_by(id=user_id).first()

    if cheker:
        cheker.profile_photo = photo
        db.commit()

        return 'фото профиля добавлено'

    return False


# Изменить данные
def change_info_db(user_id, edit_data, new_data):
    pass

# Удалить фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())

    cheker = db.query(User).filter_by(id=user_id).first()

    if cheker:
        cheker.profile_photo = 'None'
        db.commit()

        return 'фото профиля удалено'

    return False