import requests

def get_todos():

    url = "https://jsonplaceholder.typicode.com/todos"

    try: 
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        print("Error", e)
        return None

todos = get_todos()

if todos:
    completed = 0
    not_completed = 0

    for todo in todos:
        if todo["completed"]:
            completed+=1
        else:
            not_completed+=1

    print(f"Completed: {completed}")
    print(f"Not Completed: {not_completed}")
