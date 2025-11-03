from bunnet import Document
import pymongo
from datetime import datetime
class LikeArr(Document):
    id:str
    likeList:list[bool]
