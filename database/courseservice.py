from datetime import datetime

from database.models import Course
from database import get_db

def add_course_db(id, name, price, category):
    db = next(get_db())

    new_course = Course(id=id, name=name, price=price, category=category)

    db.add(new_course)
    db.commit()

    return 'Курс успешно добавлен'

def edit_course_db(id, new_name):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(id=id).first()

    if exact_course:
        exact_course.name = new_name
        db.commit()

        return "Успешно изменено"

    return False

def delete_course_db(id):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(id=id).first()

    if exact_course:
        db.delete(exact_course)
        db.commit()

        return "Успешно удалено"

    return False

def get_all_course_db():
    db = next(get_db())

    all_courses = db.query(Course).all()

    return all_courses