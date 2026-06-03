import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

#Негативный
@pytest.mark.regression
@pytest.mark.parametrize("non_existent_id", [0, 101])
def test_1_get_post_not_found(non_existent_id):
    response = requests.get(f"{BASE_URL}/posts/{non_existent_id}")
    assert response.status_code == 404

if __name__ == '__main__':
    pass
