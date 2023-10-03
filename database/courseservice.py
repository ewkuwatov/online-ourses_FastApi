from datetime import datetime

from database.models import Course, CourseCategory
from database import get_db

def add_course_db(name, name1, price, category):
    db = next(get_db())

    category_c = db.query(CourseCategory).filter_by(name=name1).first()

    new_course = Course(name=name, price=price, category=category)

    if new_course.category in category_c.name1:
        db.add(new_course)
        db.commit()

        return "Курс успешно добавлен"

    return False

def edit_course_db(name, new_name, new_price):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(name=name).first()

    if exact_course:
        exact_course.name = new_name
        exact_course.price = new_price
        db.commit()

        return "Успешно изменено"

    return False

def edit_course_category_db(name, new_category):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(name=name).first()

    if exact_course:
        exact_course.category = new_category
        db.commit()

        return "Успешно изменено"

    return False

def delete_course_db(name):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(name=name).first()

    if exact_course:
        db.delete(exact_course)
        db.commit()

        return "Успешно удалено"

    return False

def get_all_course_db():
    db = next(get_db())

    all_courses = db.query(Course).all()

    return all_courses