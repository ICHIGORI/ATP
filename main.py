import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_1_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all("id" in post for post in posts)

def test_2_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    post_data = response.json()
    assert post_data["id"] == post_id
    assert "userId" in post_data
    assert "title" in post_data
    assert "body" in post_data

def test_3_get_post_not_found():
    non_existent_id = 9999
    response = requests.get(f"{BASE_URL}/posts/{non_existent_id}")
    assert response.status_code == 404

def test_4_create_new_post():
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
    test_1_get_all_posts()
    test_2_get_post_by_id()
    test_3_get_post_not_found()
    test_4_create_new_post()
