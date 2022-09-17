
import fastapi
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from api.utils.services import create_service
from db.db_setup import get_db, async_get_db
from pydantic_schemas.services import Service, ServiceCreate

router = fastapi.APIRouter()


@router.post("/prestation", response_model=Service, status_code=201)
async def create_new_service(service: ServiceCreate, db: Session = Depends(get_db)):
       
      #user_email_exist = get_user_by_email(db=db, email=user.email)
    #if user_email_exist:
    #    raise HTTPException(
    #        status_code=400, detail="Cette utilisateur existe déjà")
    return create_service(db=db, service=service)


