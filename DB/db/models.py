from .database import Base
from sqlalchemy import Column, Integer, String


class LOG(Base):
    __tablename__ = "log"

    User = Column(String(50), primary_key=True)
    Step = Column(Integer)
    time = Column(Integer)


class user_DB(Base):
    __tablename__ = "user_db"

    user = Column(String(50), primary_key=True)
    pwd = Column(String(100))
