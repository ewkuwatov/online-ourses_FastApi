from database.models import Course, CourseCategory
from database import get_db

def add_course_db(name, discription, category, video):
    db = next(get_db())

    category_c = db.query(CourseCategory).filter_by(name=category).first()

    new_course = Course(name=name, category=category, video=video, discription=discription)

    if new_course.category in category_c.name:
        db.add(new_course)
        db.commit()

        return "Курс успешно добавлен"

    return False

def edit_course_db(name, new_name, new_video, new_discription):
    db = next(get_db())

    exact_course = db.query(Course).filter_by(name=name).first()

    if exact_course:
        exact_course.name = new_name
        exact_course.discription = new_discription
        exact_course.video = new_video

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