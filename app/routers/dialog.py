from fastapi import APIRouter
# from main import app
from typing import List
from app.schemas import UserId, User,PostText, Post, DialogMessage, DialogMessageText


router = APIRouter(
    prefix="/dialog"
)


@router.post("/{user_id}/send")
async def send_message(user_id: str, dialog_message_text: DialogMessageText):
    # Реализация логики для отправки сообщения в диалоге
    return {"message": "Успешно отправлено сообщение"}

@router.get("/{user_id}/list", response_model=List[DialogMessage])
async def get_dialog(user_id: str):
    # Реализация логики для получения сообщений в диалоге
    example_message1 = DialogMessage(from_user_id="12345", to_user_id="67890", text="Привет, как дела?")
    example_message2 = DialogMessage(from_user_id="67890", to_user_id="12345", text="Привет, все отлично!")
    return [example_message1, example_message2]