from fastapi import APIRouter,Response,status,UploadFile
from dal.tour import Tour , TourFilter


router = APIRouter(prefix="/tour")
@router.get("/all")
def api_get_all():
    return Tour.find().run()
# filter users
@router.post("/filter")
def api_get_filter(filter:TourFilter):
    return Tour.find(Tour.description == filter.description , Tour.like == filter.like).run()
"""
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
"""
# add user
@router.post("")
def api_add(tour: Tour):
    if Tour.get(tour.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        tour.save()
        return tour
# update user
@router.put("")
def api_udpate(tour: Tour):
    the_tour:Tour = Tour.get(tour.id).run() 
    if the_tour == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        tour.save()
        return tour


# # delete single user
@router.delete("/{tour_id}")
def api_delete(tour_id: str):
    the_tour:Tour = Tour.get(tour_id).run() 
    if the_tour == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_tour.delete()
        return Response(status_code=status.HTTP_200_OK)


# # find single user
@router.get("/{tour_id}")
def api_get(tour_id: str):
    the_tour:Tour = Tour.get(tour_id).run() 
    if the_tour == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_tour

    
# # add file for tour
@router.put("/file/{tour_id}")
def api_add_file(tour_id: str,file: UploadFile):
    the_tour:Tour = Tour.get(tour_id).run() 
    if the_tour == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    print("uploading file. size=",file.size)
    the_tour.add_file(file.file,file.content_type)

# # get a file for tour
@router.get("/file/{tour_id}")
def api_get_file(tour_id: str):
    the_tour:Tour = Tour.get(tour_id).run() 
    if the_tour == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    f_data,media_type = the_tour.get_file()
    print(media_type)
    if f_data == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(content=f_data, media_type=media_type)