from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: str
    category_id: int