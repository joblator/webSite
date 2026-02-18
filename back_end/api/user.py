from fastapi import APIRouter,Response,status,UploadFile

from dal.user import User,UserLogin

router = APIRouter(prefix="/user")
# filter users

@router.get("/all")
def api_get_all():
    return User.find().run()

# login
@router.post("/login")
def api_login(ul: UserLogin) :
    the_user:User = User.get(ul.email).run() 
    if the_user == None:
        return Response("user not found",status_code=status.HTTP_404_NOT_FOUND)
    elif the_user.password != ul.password:
        return Response("incorrect password",status_code=status.HTTP_404_NOT_FOUND)        
    else:
        return the_user

# add user
@router.post("")
def api_add(user: User):
    if User.get(user.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        user.save()
        return user
# update user
@router.put("")
def api_udpate(user: User):
    the_user:User = User.get(user.id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        user.save()
        return user


# # delete single user
@router.delete("/{user_id}")
def api_delete(user_id: str):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_user.delete()
        return Response(status_code=status.HTTP_200_OK)


# # find single user
@router.get("/{user_id}")
def api_get(user_id: str):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_user


