import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

#Позитивный
@pytest.mark.smoke
@pytest.mark.regression
def test_1_put():
    data_id = 1
    new_post = {
        "id": data_id,
        "title": "foo",
        "body": "bar",
        "userId": data_id,
    }
    response = requests.put(f"{BASE_URL}/posts/{data_id}", json=new_post)
    assert response.status_code == 200
    data_json = response.json()
    assert data_json["title"] == new_post["title"]
    assert data_json["body"] == new_post["body"]
    assert data_json["userId"] == new_post["userId"]
    assert data_json["id"] == data_id

if __name__ == '__main__':
    pass
