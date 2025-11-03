from bunnet import Document
import pymongo
from datetime import datetime
class FavoritesList(Document):
    #id: made automatically
    description:str
    like:bool
    favorite:bool
