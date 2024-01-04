from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText


router = APIRouter(
    prefix="/friends"
)

@router.put("/set/{user_id}")
async def set_friend(user_id: str):
    # Реализация логики для установки друга для пользователя
    return {"message": "Пользователь успешно указал своего друга"}


@router.get("/get/{user_id}")
async def get_friends(user_id: str):
    # Реализация логики для установки друга для пользователя
    friends = [1, 2, 4, 5] # id пользоателей, которые являются друзьями
    return {"friends": friends}

@router.put("/delete/{user_id}")
async def delete_friend(user_id: str):
    # Реализация логики для удаления друга у пользователя
    return {"message": "Пользователь успешно удалил из друзей пользователя"}
