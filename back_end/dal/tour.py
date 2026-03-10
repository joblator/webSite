from bunnet import Document
from pydantic import BaseModel
import pymongo
import gridfs
from datetime import datetime
from dal.db import get_db
class TourFilter(BaseModel):
    description:str
    location:str
class Tour(Document):
    tourMaker:str
    description:str
    like:bool
    favorite:bool
    location:str

    def validate_tour(self) -> tuple[bool, str]:
        if any(char.isdigit() for char in self.location):
            return False, "There cant be a number in location"
        if len(self.description) < 4:
            return False, "description must be at least 4 characters"
        return True, "" 


    def add_file(self,file_data,content_type):
        # TODO: check if the user exits before adding the file
        # TODO: delete old files before if needed
        fs = gridfs.GridFS(get_db())
        fs.put(file_data,user_id=str(self.id),contentType=content_type) # can add more custom fields like filename, description ....etc

    # in case there is only one image per user
    def get_file(self):
        fs = gridfs.GridFS(get_db())
        data = get_db().fs.files.find_one({'user_id':str(self.id)})
        if data == None:
            return None,None
        
        f_id = data['_id']
        output_data = fs.get(f_id).read()
        return output_data,data['contentType']
