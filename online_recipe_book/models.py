from sqlalchemy import Column, Integer, String, Text
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)
    cuisine = Column(String)
    difficulty = Column(String)