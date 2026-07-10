import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error", e)
        return None

users = get_users()

if users:
    for i, user in enumerate(users[:5], start = 1):
        print(f"{i}.{user['name']} - {user['email']}")