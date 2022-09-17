import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "6eab9cc206007b270a820bcd1ad4819aa4854210f7eb79b219a757b48a4de96e"  # should be kept secret
#JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']should be kept secret