import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

#Позитивный
@pytest.mark.smoke
@pytest.mark.regression
def test_1_create_new_post_with_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data_json = response.json()
    assert data_json["title"] == new_post["title"]
    assert data_json["body"] == new_post["body"]
    assert data_json["userId"] == new_post["userId"]
    assert "id" in data_json

@pytest.mark.regression
def test_2_create_new_post_with_put():
    new_post = {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=new_post)
    assert response.status_code == 200
    data_json = response.json()
    assert data_json["title"] == new_post["title"]
    assert data_json["body"] == new_post["body"]
    assert data_json["userId"] == new_post["userId"]
    assert "id" in data_json

@pytest.mark.regression
def test_3_create_new_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    created_data = response.json()
    assert created_data["title"] == new_post["title"]
    assert created_data["body"] == new_post["body"]
    assert created_data["userId"] == new_post["userId"]
    assert "id" in created_data

if __name__ == '__main__':
    pass
