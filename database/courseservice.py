from datetime import datetime

from database.models import Course
from database import get_db

def add_course_db(category_id, name, description, price):
    db = next(get_db())

    new_course = Course(category_id=category_id, name=name, description=description, price=price, publish_date=datetime.now())

    db.add(new_course)
    db.commit()

    return 'Курс успешно добавлен'