from .database import Base
from sqlalchemy import Column, Integer, String


class LOG(Base):
    __tablename__ = "LOGs"

    User = Column(String, primary_key=True)
    Step = Column(Integer)
    time = Column(Integer)


class user_DB(Base):
    __tablename__ = "user_DB"

    user = Column(String, primary_key=True)
    pwd = Column(String)
