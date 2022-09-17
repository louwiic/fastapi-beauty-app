import imp
from unittest import result
from sqlalchemy.orm import Session

from db.models.User import User

from pydantic_schemas.users import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()
 

async def get_user_by_email(db: AsyncSession, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(
                firstname=user.firstname,
                lastname=user.lastname,
                email=user.email, 
                role=user.role,
                password= user.password,
                phone= user.phone,
                address= user.address,
                city= user.city,
                zipcode= user.zipcode,
                lat= user.lat,
                lng= user.lng,
                avatar=user.avatar
                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


''' def get_user_courses(db: Session, user_id: int):
    course = db.query(Course).filter(Course.user_id == user_id).all()
    return course
 '''