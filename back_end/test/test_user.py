from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.user import * 
import random
import pytest

client = TestClient(app)

# generates a new random user
def generate_user(is_admin)->User:
    name = 'test_'+str(random.randint(1, 1000))
    password = 'pass_'+str(random.randint(1, 1000))
    user_id = 'email_'+str(random.randint(1, 1000))+'@gmail.com'
    new_user:User = User(id=user_id,password=password,is_admin=is_admin,dob=datetime(2008,2,24),name=name)
    return new_user



def test_add():
    new_user:User = generate_user(True)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_user.id
    assert response.json()['password'] == new_user.password

    # try to add the same user again, should get 400
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_user.delete()


def test_get_all():
    # find how many users are there
    response = client.get("/user/all")
    assert response.status_code == status.HTTP_200_OK
    count = len(response.json())

    # add a new user
    new_user:User = generate_user(True)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # make sure one user was added to the all response
    response = client.get("/user/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == count+1

    new_user.delete()
def test_login():
    new_user:User = generate_user(True)
    login_user:UserLogin = UserLogin(email=new_user.id,password=new_user.password)
    response = client.post("/user/login",data= login_user.model_dump_json())
    #check if it doesent find a user
    assert response.text == "user not found"
    assert response.status_code == status.HTTP_404_NOT_FOUND

    #adds new user
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    #checks if login works
    response = client.post("/user/login",data=login_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == login_user.email
    assert response.json()['password'] == login_user.password
    new_user.delete()

    
def test_update():
    new_user = generate_user(True)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    new_user.name = "boris"
    response = client.put("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_user.id
    assert response.json()['password'] == new_user.password
    assert response.json()['dob'] == new_user.dob.strftime('%Y-%m-%dT%H:%M:%S')
    assert response.json()['is_admin'] == new_user.is_admin
    assert response.json()['name'] == new_user.name
    new_user.delete()
    


def test_Delete():
    new_user = generate_user(True)
    response = client.delete("/user/"+new_user.id)
    #check delete before adding the user
    assert response.status_code == status.HTTP_404_NOT_FOUND
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    response = client.delete(f"/user/"+new_user.id)
    assert response.status_code == status.HTTP_200_OK




def test_Find():
    new_user = generate_user(True)
    response = client.get("/user/"+new_user.id)
    #check delete before adding the user
    assert response.status_code == status.HTTP_404_NOT_FOUND
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    response = client.get(f"/user/"+new_user.id)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_user.id
    assert response.json()['password'] == new_user.password
    assert response.json()['dob'] == new_user.dob.strftime('%Y-%m-%dT%H:%M:%S')
    assert response.json()['is_admin'] == new_user.is_admin
    assert response.json()['name'] == new_user.name
    new_user.delete()




