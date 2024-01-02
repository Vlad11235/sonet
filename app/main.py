from fastapi import FastAPI, HTTPException, Body, APIRouter

from app.routers import index, post, user, login, dialog, friends


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(dialog.router)
app.include_router(friends.router)
app.include_router(index.router)


# Запускаем FastAPI приложение с помощью uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
