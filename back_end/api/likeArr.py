from dal.likeArr import LikeArr
from fastapi import APIRouter,Response,status,UploadFile

router = APIRouter(prefix="/likes")
# add user
@router.post("")
def api_add(like_List: LikeArr):
    if LikeArr.get(like_List.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        like_List.save()
        return like_List
# update user
@router.put("")
def api_udpate(like_List: LikeArr):
    the_list:LikeArr = LikeArr.get(like_List.id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        like_List.save()
        return like_List


# # delete single user
@router.delete("/{list_id}")
def api_delete(list_id: str):
    the_list:LikeArr = LikeArr.get(list_id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_list.delete()
        return Response(status_code=status.HTTP_200_OK)


# # find single user
@router.get("/{list_id}")
def api_get(list_id: str):
    the_list:LikeArr = LikeArr.get(list_id).run() 
    if the_list == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_list