from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Схемы данных
class UserId(BaseModel):
    id: str

class BirthDate(BaseModel):
    birthdate: str

class User(BaseModel):
    id: str
    first_name: str
    second_name: str
    birthdate: str
    biography: str
    gender: str
    city: str
    

class PostText(BaseModel):
    text: str

class PostId(BaseModel):
    id: str

class DialogMessageText(BaseModel):
    text: str

class DialogMessage(BaseModel):
    from_user_id: str
    to_user_id: str
    text: str

class Post(BaseModel):
    id: str
    text: str
    author_user_id: str


# class PostBase(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# class PostCreate(PostBase):
#     pass


# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime

#     class Config:
#         orm_mode = True





# class PostOut(BaseModel):
#     Post: Post
#     votes: int

#     class Config:
#         orm_mode = True


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str



# class PostCreate(PostBase):
#     pass


# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime

#     class Config:
#         orm_mode = True


# class Post(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: UserOut

#     class Config:
#         orm_mode = True


# class PostOut(BaseModel):
#     Post: Post
#     votes: int

#     class Config:
#         orm_mode = True


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     id: Optional[str] = None[str] 