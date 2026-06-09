from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Recipe
import schemas

app = FastAPI(title="Recipe API")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/recipes/{recipe_id}", response_model=schemas.RecipeResponse)
def update_recipe(
    recipe_id: int,
    updated_data: schemas.RecipeCreate,
    db: Session = Depends(get_db)
):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        return {"error": "Recipe not found"}

    # update fields
    recipe.name = updated_data.name
    recipe.description = updated_data.description
    recipe.ingredients = updated_data.ingredients
    recipe.instructions = updated_data.instructions
    recipe.cuisine = updated_data.cuisine
    recipe.difficulty = updated_data.difficulty

    db.commit()
    db.refresh(recipe)

    return recipe


@app.post("/recipes", response_model=schemas.RecipeResponse)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@app.get("/recipes", response_model=list[schemas.RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()



@app.get("/recipes/{recipe_id}", response_model=schemas.RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()



@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    db.delete(recipe)
    db.commit()
    return {"message": "Deleted successfully"}