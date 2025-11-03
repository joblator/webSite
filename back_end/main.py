from  dal.user import User
from dal.favoriteArr import FavoritesList
from dal.likeArr import LikeArr
from dal.tour import Tour 
from dal.db import init_db
from fastapi import FastAPI
import uvicorn

from api.user import router as user_router
# from api.task import router as task_router


if __name__ == "__main__":
    uvicorn.run("main:app", port=8090,reload=True)
else:
    init_db([User,Tour,LikeArr,FavoritesList])
    app = FastAPI()
    app.include_router(user_router)