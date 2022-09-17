
import fastapi
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from api.utils.category import create_category
from db.db_setup import get_db, async_get_db
from pydantic_schemas.category import Category, CategoryCreate

router = fastapi.APIRouter()


@router.post("/category", response_model=Category, status_code=201)
async def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
       
      #user_email_exist = get_user_by_email(db=db, email=user.email)
    #if user_email_exist:
    #    raise HTTPException(
    #        status_code=400, detail="Cette utilisateur existe déjà")
    return create_category(db=db, category=category)


