from bunnet import Document

class FavoritesList(Document):
    id:str #email of the user
    favList:list[str]
