from datetime import datetime

from database.models import CourseCategory
from database import get_db

def add_category_db(name):
    db = next(get_db())

    new_category = CourseCategory(name=name)

    db.add(new_category)
    db.commit()

    return 'Категория успешно добавлено'

def edit_category_db(name, new_name):
    db = next(get_db())

    exact_category = db.query(CourseCategory).filter_by(name=name).first()

    if exact_category:
        exact_category.name = new_name
        db.commit()

        return "Успешно изменено"

    return False

def delete_categoryt_db(name):
    db = next(get_db())

    exact_category = db.query(CourseCategory).filter_by(name=name).first()

    if exact_category:
        db.delete(exact_category)
        db.commit()

        return "Успешно удалено"

    return False

def get_all_category_db():
    db = next(get_db())

    all_category = db.query(CourseCategory).all()

    return all_category