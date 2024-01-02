from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText


router = APIRouter(
    prefix="/user"
)

@router.post("/register")
async def register(user: User):
    # ваша логика регистрации
    # возвращаем идентификатор пользователя
    return {"user_id": "e4d2e6b0-cde2-42c5-aac3-0b8316f21e58"}


@router.get("/get/{id}", response_model=User)
async def get_user(id: str):
    # Реализация логики для получения информации о пользователе по идентификатору
    # Замените этот код на вашу собственную реализацию
    example_user = User(id="12345", first_name="John", second_name="Doe", birthdate="1990-01-01", biography="Some bio", city="New York")
    return example_user

@router.get("/search", response_model=List[User])
async def search_users(first_name: str, last_name: str):
    # Реализация логики для поиска пользователей по имени и фамилии
    # Замените этот код на вашу собственную реализацию
    example_user1 = User(id="12345", first_name="John", second_name="Doe", birthdate="1990-01-01", biography="Some bio", city="New York")
    example_user2 = User(id="67890", first_name="Jane", second_name="Smith", birthdate="1995-05-05", biography="Some other bio", city="Los Angeles")
    return [example_user1, example_user2]
