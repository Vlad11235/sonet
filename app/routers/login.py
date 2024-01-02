from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText


router = APIRouter(
    prefix="/login"
)


@router.post("/")
async def login(user_id: UserId, password: str):
    # ваша логика аутентификации
    # возвращаем токен
    return {"token": "e4d2e6b0-cde2-42c5-aac3-0b8316f21e58"}