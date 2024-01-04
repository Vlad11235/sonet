from fastapi import FastAPI, HTTPException, Body, APIRouter
from fastapi.security import CSRFProtect
from passlib.context import CryptContext
from app.routers import index, post, user, login, dialog, friends


app = FastAPI()
csrf = CSRFProtect(app)

# настройки для хеширования пароля
pwd_context = CryptContext(schemes=["pbkdf2_sha512"], deprecated="auto")

app.include_router(post.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(dialog.router)
app.include_router(friends.router)
app.include_router(index.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)