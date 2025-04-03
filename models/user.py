from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('DbBlog',back_populates='user')