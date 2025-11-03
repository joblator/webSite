from fastapi import APIRouter,Response,status,UploadFile

from dal.user import User,UserFilter,UserLogin

router = APIRouter(prefix="/user")
@router.get("/all")
def api_get_all():
    return User.find().run()
# filter users
@router.post("/filter")
def api_get_filter(filter:UserFilter):
    return User.find(User.name == filter.name , User.is_admin == filter.is_admin).run()


# login
@router.post("/login")
def api_login(ul: UserLogin) :
    the_user:User = User.get(ul.name).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    elif the_user.password != ul.password:
        return Response(status_code=status.HTTP_404_NOT_FOUND)        
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

    
# # add file for user
@router.put("/file/{user_id}")
def api_add_file(user_id: str,file: UploadFile):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    print("uploading file. size=",file.size)
    the_user.add_file(file.file,file.content_type)

# # get a file for user
@router.get("/file/{user_id}")
def api_get_file(user_id: str):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    f_data,media_type = the_user.get_file()
    print(media_type)
    if f_data == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(content=f_data, media_type=media_type)
