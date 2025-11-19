from pymongo import MongoClient
from bunnet import Document
from datetime import datetime 
from pydantic import BaseModel
import gridfs
from dal.db import get_db
class UserLogin(BaseModel):
    email: str
    password: str
class UserFilter(BaseModel):
    name:str
    is_admin: bool
class User(Document):
    id:str #the email
    name:str
    dob:datetime
    is_admin:bool
    password:str

    # in case there are many images per user, use with get_file_by_file_id
    def get_all_file_ids(self):
        res=[]
        db = User.connect2DB()
        fs = gridfs.GridFS(db)
        data = db.fs.files.find({'user_id':str(self.id)})
        if data == None:
            return None,None
        for d in data:
            res.append(d['_id'])
        return res

    def get_file_by_file_id(file_id):
        db = User.connect2DB()
        fs = gridfs.GridFS(db)
        data = db.fs.files.find_one({'_id':file_id})
        if data == None:
            return None
        print("found file, data=",data)
        f_id = data['_id']
        output_data = fs.get(f_id).read()
        return output_data,data['contentType']

    # delete all fiels for the user, return how mnay files were deleted
    def delete_all_files(self):
        db = User.connect2DB()
        fs = gridfs.GridFS(db)
        files = self.get_all_file_ids()
        for f_id in files:
            print("deleting file:"+str(f_id))
            fs.delete(f_id)
        return len(files)





    
