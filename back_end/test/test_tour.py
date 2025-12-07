from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.tour import * 
import random

client = TestClient(app)

# generates a new random user
def generate_Tour(like:bool,favorite:bool)->Tour:
    description = 'description_'+str(random.randint(1, 1000))
    new_tour:Tour = Tour(description=description,like=like,favorite=favorite)
    return new_tour



def test_add():
    new_tour:Tour = generate_Tour(True,False)
    response = client.post("/tour",data=new_tour.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['description'] == new_tour.description
    assert response.json()['like'] == new_tour.like
    assert response.json()['favorite'] == new_tour.favorite
    new_tour.id = response.json()['_id']

    

    # try to add the same user again, should get 400
    response = client.post("/tour",data=new_tour.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_tour.delete()


def test_get_all():
    # find how many users are there
    response = client.get("/tour/all")
    assert response.status_code == status.HTTP_200_OK
    count = len(response.json())

    # add a new user
    new_tour:Tour = generate_Tour(True,False)
    response = client.post("/tour",data=new_tour.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # make sure one user was added to the all response
    response = client.get("/tour/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == count+1
    new_tour.delete()



def test_update():
    new_tour = generate_Tour(True,False)
    response = client.post("/tour",data=new_tour.model_dump_json())
    new_tour.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    new_tour.description = "boris"
    response = client.put("/tour",data=new_tour.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_tour.id
    assert response.json()['description'] == new_tour.description
    assert response.json()['like'] == new_tour.like
    assert response.json()['favorite'] == new_tour.favorite
    new_tour.delete()
    


def test_Delete():
    new_tour = generate_Tour(True,False)
    #check delete before adding the user
    response = client.post("/tour",data=new_tour.model_dump_json())
    new_tour.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/tour/"+str(new_tour.id))
    assert response.status_code == status.HTTP_200_OK




def test_Find():
    new_tour = generate_Tour(True,False)
    response = client.post("/tour",data=new_tour.model_dump_json())
    new_tour.id = response.json()['_id']
    assert response.status_code == status.HTTP_200_OK
    response = client.get(f"/tour/"+str(new_tour.id))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['description'] == new_tour.description
    new_tour.delete()