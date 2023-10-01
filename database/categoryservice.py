from datetime import datetime

from database.models import CourseCategory
from database import get_db

def add_category_db(id, name):
    db = next(get_db())

    new_category = CourseCategory(id=id,
                                  name=name)

    db.add(new_category)
    db.commit()

    return 'Категория успешно добавлено'

def edit_category_db(category_id, new_name):
    db = next(get_db())

    exact_category = db.query(CourseCategory).filter_by(category_id=category_id, id=id).first()

    if exact_category:
        exact_category.name = new_name
        db.commit()

        return "Успешно изменено"

    return False

def delete_categoryt_db(category_id):
    db = next(get_db())

    exact_category = db.query(CourseCategory).filter_by(id=category_id).first()

    if exact_category:
        db.delete(exact_category)
        db.commit()

        return "Успешно удалено"

    return False

def get_all_category_db():
    db = next(get_db())

    all_category = db.query(CourseCategory).all()

    return all_category