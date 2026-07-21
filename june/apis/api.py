import requests

def get_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    return response.json()

posts = get_posts()

if posts:
    for post in posts:
        if post["userId"] == 1:
            print(f"{post["title"]}")