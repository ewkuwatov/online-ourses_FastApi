from fastapi import FastAPI

from user.user_api import user_router
from category.category_api import category_router
from course.course_api import course_router
from comment.comment_api import comment_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(category_router)
app.include_router(course_router)
app.include_router(comment_router)


@app.get('/hello')
async def hello():
    return {'message': 'Hello world'}

