import requests

def get_comment():

    url = "https://jsonplaceholder.typicode.com/comments"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        print("Error", e)
        return None
    
comments = get_comment()

if comments:
    for comment in comments:
        if comment["postId"] == 1:
            print(f"Name: {comment['name']}")
            print(f"Email: {comment['email']}")
            print("-" * 30)