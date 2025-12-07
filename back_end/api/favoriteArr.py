from dal.favoriteArr import FavoritesList
from fastapi import APIRouter,Response,status,UploadFile

router = APIRouter(prefix="/favorites")
# add user
@router.post("")
def api_add(favList: FavoritesList):
    if FavoritesList.get(favList.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        favList.save()
        return favList
    
@router.get("/all")
def api_get_all():
    return FavoritesList.find().run()
# update user
@router.put("")
def api_udpate(favList: FavoritesList):
    the_list:FavoritesList = FavoritesList.get(favList.id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        favList.save()
        return favList


# # delete single user
@router.delete("/{list_id}")
def api_delete(list_id: str):
    the_list:FavoritesList = FavoritesList.get(list_id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_list.delete()
        return Response(status_code=status.HTTP_200_OK)


# # find single user
@router.get("/{list_id}")
def api_get(list_id: str):
    the_list:FavoritesList = FavoritesList.get(list_id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_list