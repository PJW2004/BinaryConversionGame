from .database import Base
from sqlalchemy import Column, Integer, String


class LOG(Base):
    __tablename__ = "log"
    index = Column(Integer, primary_key=True)
    User = Column(String(50))
    Step = Column(Integer)
    time = Column(Integer)


class user_DB(Base):
    __tablename__ = "user_db"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(50))
    pwd = Column(String(100))

