
import email
import imp
import logging
import fastapi
from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from api.utils.etablissements import create_etablissement
from db.db_setup import get_db, async_get_db
from pydantic_schemas.etablissements import Etablissement, EtablissementCreate
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from utils import password_context

router = fastapi.APIRouter()


@router.post("/etablissements", response_model=Etablissement, status_code=201)
async def create_new_etablissement(etablissement: EtablissementCreate, db: Session = Depends(get_db)):
       
      #user_email_exist = get_user_by_email(db=db, email=user.email)
    #if user_email_exist:
    #    raise HTTPException(
    #        status_code=400, detail="Cette utilisateur existe déjà")
    return create_etablissement(db=db, etablissement=etablissement)


