from  dal.user import User
from dal.favoriteArr import FavoritesList
from dal.likeArr import LikeArr
from dal.tour import Tour 
from dal.db import init_db
from fastapi import FastAPI
import uvicorn

from api.user import router as user_router
from api.tour import router as tour_router
from api.likeArr import router as like_router
from api.favoriteArr import router as fav_router




if __name__ == "__main__":
    uvicorn.run("main:app", port=8090,reload=True)
else:
    init_db([User,Tour,LikeArr,FavoritesList])
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(tour_router)
    app.include_router(fav_router)
    app.include_router(like_router)