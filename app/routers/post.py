from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText
# import ftom uuid4


router = APIRouter(
    prefix="/post"
)
posts = []

@router.post("/create", response_model=Post)
async def create_post(post_text: PostText):
    # post = Post(id=str(uuid4()), text=post_text.text)
    # posts.append(post)
    # return post
    return {"id": "1d535fd6-7521-4cb1-aa6d-031be7123c4d"}

# @router.post("/create")
# async def create_post(post_text: PostText):
#     # Реализация логики для создания поста
#     # Замените этот код на вашу собственную реализацию
#     return {"id": "1d535fd6-7521-4cb1-aa6d-031be7123c4d"}

@router.put("/update")
async def update_post(post_id: str, post_text: PostText):
    # Реализация логики для изменения поста
    # Замените этот код на вашу собственную реализацию
    return {"message": "Успешно изменен пост"}

@router.put("/delete/{id}")
async def delete_post(id: str):
    # Реализация логики для удаления поста
    # Замените этот код на вашу собственную реализацию
    return {"message": "Успешно удален пост"}

@router.get("/get/{id}", response_model=Post)
async def get_post(id: str):
    # Реализация логики для получения информации о посте по его идентификатору
    # Замените этот код на вашу собственную реализацию
    example_post = Post(id="1d535fd6-7521-4cb1-aa6d-031be7123c4d", text="Some post text", author_user_id="12345")
    return example_post

@router.get("/feed", response_model=List[Post])
async def get_post_feed(offset: int = 0, limit: int = 10):
    # Реализация логики для получения ленты постов
    # Замените этот код на вашу собственную реализацию
    example_post1 = Post(id="1d535fd6-7521-4cb1-aa6d-031be7123c4d", text="Some post text 1", author_user_id="12345")
    example_post2 = Post(id="6f49a45a-83b7-4920-9e3c-4af5c893d679", text="Some post text 2", author_user_id="67890")
    return [example_post1, example_post2]



