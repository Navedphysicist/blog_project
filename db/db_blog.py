from sqlalchemy.orm import Session
from models.blog import DbBlog
from schemas.blog import Blog


def create_blog(db:Session,request:Blog,user_id:int):
    new_blog = DbBlog(
        title = request.title,
        content = request.content,
        user_id = user_id
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all_blogs(db:Session):
     # raise excetipion
    return db.query(DbBlog).all()



