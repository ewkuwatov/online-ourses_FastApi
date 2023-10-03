from database.models import Course, Comment
from database import get_db

def add_comment_db(user, comment, course):
    db = next(get_db())

    course_fk = db.query(Course).filter_by(name=course).first()

    new_comment = Comment(user=user, comment=comment, course=course)

    if new_comment.course in course_fk.name:
        db.add(new_comment)
        db.commit()

        return "Комментарий успешно добавлен"

    return False

def edit_comment_db(id, new_comment):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=id).first()

    if exact_comment:
        exact_comment.comment = new_comment

        db.commit()

        return "Успешно изменено"

    return False

def get_all_comment_db():
    db = next(get_db())

    all_comment = db.query(Comment).all()

    return all_comment