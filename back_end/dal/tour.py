from bunnet import Document
from pydantic import BaseModel
import pymongo
import gridfs
from datetime import datetime
from dal.db import get_db
class TourFilter(BaseModel):
    description:str
    like:bool  #if the user liked the tour
class Tour(Document): 
    description:str
    like:bool
    favorite:bool


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
