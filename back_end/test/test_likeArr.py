from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.likeArr import * 
import random

client = TestClient(app)

# generates a new random user
def generate_likeArr()->LikeArr:
    id = 'email_'+str(random.randint(1, 1000))+'@gmail.com' 
    likeList = []
    new_likeArr:LikeArr = LikeArr(id=id,likeList=likeList)
    return new_likeArr



def test_add():
    new_likeArr:LikeArr = generate_likeArr()
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_likeArr.id
    assert response.json()['likeList'] == new_likeArr.likeList

    
    # try to add the same user again, should get 400
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_likeArr.delete()


def test_get_all():
    # find how many users are there
    response = client.get("/likes/all")
    assert response.status_code == status.HTTP_200_OK
    count = len(response.json())

    # add a new user
    new_likeArr:LikeArr = generate_likeArr()
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # make sure one user was added to the all response
    response = client.get("/likes/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == count+1
    new_likeArr.delete()



def test_update():
    new_likeArr = generate_likeArr( )
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    new_likeArr.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    new_likeArr.likeList.append("hello")
    response = client.put("/likes",data=new_likeArr.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_likeArr.id
    assert response.json()['likeList'] == new_likeArr.likeList
    new_likeArr.delete()
    


def test_Delete():
    new_likeArr = generate_likeArr( )
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    new_likeArr.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/likes/"+str(new_likeArr.id))
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/likes/"+str(new_likeArr.id))
    assert response.status_code == status.HTTP_404_NOT_FOUND



def test_Find():
    new_likeArr = generate_likeArr( )
    response = client.post("/likes",data=new_likeArr.model_dump_json())
    new_likeArr.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.get(f"/likes/"+str(new_likeArr.id))
    assert response.status_code == status.HTTP_200_OK
    assert new_likeArr.likeList == response.json()['likeList']
    new_likeArr.delete()