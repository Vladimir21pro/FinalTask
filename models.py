from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    phone = Column(String)
    fam = Column(String)
    name = Column(String)
    otc = Column(String)

    perevals = relationship("Pereval", back_populates="user")


class Pereval(Base):
    __tablename__ = "perevals"
    id = Column(Integer, primary_key=True)
    status = Column(String, default="new")
    beauty_title = Column(String)
    title = Column(String)
    other_titles = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="perevals")
