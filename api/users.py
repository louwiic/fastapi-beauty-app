
import fastapi
from fastapi.security import OAuth2PasswordBearer
from typing import List
from fastapi import HTTPException, Depends,status, Request
from pydantic import HttpUrl
from sqlalchemy.orm import Session
from api.utils.users import  get_user_by_email, get_users, create_user, get_user
from auth.auth_handler import JWTBearer
from auth.jwt_handler import create_access_token, create_refresh_token, decode_refreshToken, decode_token
from db.db_setup import get_db, async_get_db
from pydantic_schemas.users import TokenJWT, User, UserCreate, UserEditPassword, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from utils import password_context, verify_password
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
 
router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db=db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db),dbAsync: AsyncSession = Depends(async_get_db)):
    user.password = password_context.hash(user.password)
    user_email_exist = await get_user_by_email(db=dbAsync, email=user.email)
    if user_email_exist:
        raise HTTPException(
            status_code=400, detail="Cette utilisateur existe déjà")
    return create_user(db=db, user=user)



@router.post('/refresh')
async def refresh(token: TokenJWT, db: AsyncSession = Depends(async_get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
         # Only accept post requests
        payload = decode_refreshToken(token.token)
        user_id = int(payload['sub'])
        if payload is None:
            raise credentials_exception
        # Check if token is not expired
        # Validate email
        user_db = await get_user(db=db, user_id=user_id)
        if user_db:
            new_access_token = create_access_token(user_id)
            return {"access_token": new_access_token}
    except JWTError:
        raise credentials_exception


@router.post("/login",)
async def sign(user: UserLogin, db: AsyncSession = Depends(async_get_db)):
    user_db = await get_user_by_email(db=db, email=user.email)
    errorLogin = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not user_db:
        raise errorLogin
    if not verify_password(user.password, user_db.password):
        raise errorLogin

    return {
        "access_token": create_access_token(user_db.id),
        "refresh_token": create_refresh_token(user_db.id),
    }

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)

@router.post("/forgotpassword",)
async def change_password(user: UserEditPassword,token: str = Depends(reuseable_oauth), db: AsyncSession = Depends(async_get_db)):
    
    return {"token"}
    user_db = await get_user_by_email(db=db, email=user.email)
    errorLogin = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not user_db:
        raise errorLogin
    if not verify_password(user.password, user_db.password):
        raise errorLogin

 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/auth/users/{user_id}",  dependencies=[Depends(JWTBearer())], response_model=User,)
async def read_user_by_id(user_id: int, token: str = Depends(oauth2_scheme),  db: AsyncSession = Depends(async_get_db)):
    
    payload = decode_token(token) #info user connected
    userId = int(payload['sub'])
    print(userId)
    userById = await get_user(db=db, user_id=userId)
    if userById is None:
        raise HTTPException(status_code=404, detail="User not found")
    return userById


