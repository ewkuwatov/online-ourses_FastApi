from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    profile_photo = Column(String)
    password = Column(String)

    reg_date = Column(DateTime)

class CourseCategory(Base):
    __tablename__ = 'courses_category'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    price = Column(String)
    category = Column(Integer, ForeignKey(CourseCategory.id))
    course_photo = Column(String)
