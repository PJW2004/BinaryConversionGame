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

    user = Column(String(50), primary_key=True, index=True)
    pwd = Column(String(100))
    id = Column(Integer)
