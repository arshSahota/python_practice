# import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users/1"
# )

# def test_get_user():

#     assert response.status_code == 200

# def test_user_id():

#     data = response.json()

#     assert data["id"] == 1

# def test_device_response():

#     data = response.json()

#     assert "id" in data
#     assert "name" in data