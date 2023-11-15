from sqlalchemy import Column, Integer, String

from app1.db import Base


class Character(Base):
    __tablename__="Character"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    resourceURI = Column(String, nullable=False)


character = Character.__tablename__