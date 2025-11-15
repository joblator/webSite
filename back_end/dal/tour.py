from bunnet import Document
from pydantic import BaseModel
import pymongo
from datetime import datetime
class TourFilter(BaseModel):
    description:str
    like:bool
class Tour(Document):
    #id: made automatically
    description:str
    like:bool
    favorite:bool
