from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText


router = APIRouter(
    prefix=""
)

@router.get("/")
@router.get("/index")
async def get_hello():
    # логика регистрации
    # возвращаем идентификатор пользователя
    return {"test": "Hello"}
