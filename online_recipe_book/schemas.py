from pydantic import BaseModel

class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: str
    instructions: str
    cuisine: str
    difficulty: str


class RecipeResponse(RecipeCreate):
    id: int

    class Config:
        from_attributes = True