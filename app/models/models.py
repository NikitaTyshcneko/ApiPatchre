from sqlalchemy import Column, Integer, String

from app.db import Base


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    resourceURI = Column(String, nullable=False)


character = Card.__tablename__
