from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.favoriteArr import * 
import random

client = TestClient(app)

# generates a new random user
def generate_FavoritesList()->FavoritesList:
    id = 'email_'+str(random.randint(1, 1000))+'@gmail.com' 
    favList = []
    new_FavoritesList:FavoritesList = FavoritesList(id=id,favList=favList)
    return new_FavoritesList



def test_add():
    new_FavoritesList:FavoritesList = generate_FavoritesList()
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_FavoritesList.id
    assert response.json()['favList'] == new_FavoritesList.favList

    
    # try to add the same user again, should get 400
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_FavoritesList.delete()


def test_get_all():
    # find how many users are there
    response = client.get("/favorites/all")
    assert response.status_code == status.HTTP_200_OK
    count = len(response.json())

    # add a new user
    new_FavoritesList:FavoritesList = generate_FavoritesList()
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # make sure one user was added to the all response
    response = client.get("/favorites/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == count+1
    new_FavoritesList.delete()



def test_update():
    new_FavoritesList = generate_FavoritesList( )
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    new_FavoritesList.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    new_FavoritesList.favList.append("hello")
    response = client.put("/favorites",data=new_FavoritesList.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_FavoritesList.id
    assert response.json()['favList'] == new_FavoritesList.favList
    new_FavoritesList.delete()
    


def test_Delete():
    new_FavoritesList = generate_FavoritesList( )
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    new_FavoritesList.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/favorites/"+str(new_FavoritesList.id))
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/favorites/"+str(new_FavoritesList.id))
    assert response.status_code == status.HTTP_404_NOT_FOUND



def test_Find():
    new_FavoritesList = generate_FavoritesList( )
    response = client.post("/favorites",data=new_FavoritesList.model_dump_json())
    new_FavoritesList.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.get(f"/favorites/"+str(new_FavoritesList.id))
    assert response.status_code == status.HTTP_200_OK
    assert new_FavoritesList.favList == response.json()['favList']
    new_FavoritesList.delete()