from pymongo import MongoClient
from bunnet import init_bunnet
from functools import lru_cache


@lru_cache()
def get_db():    
    print("connecting to DB...")
    client = MongoClient("mongodb+srv://janjoelbonisch_db_user:janjoelbonisch_db_password@cluster0.zbnxxqz.mongodb.net/?appName=Cluster0")
    print("connected to DB.")
    return client.tourSite


def init_db(document_models: list = None):
    init_bunnet(database=get_db(), document_models=document_models)

