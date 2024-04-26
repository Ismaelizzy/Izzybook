from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, index=True)
    postId = Column(String, index=True)
    userId = Column(String, index=True)
    content = Column(String)
    
