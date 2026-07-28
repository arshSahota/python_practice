purchases = [
    {"user": "Alice", "item": "Book"},
    {"user": "Bob", "item": "Pen"},
    {"user": "Alice", "item": "Notebook"},
    {"user": "Bob", "item": "Pencil"},
    {"user": "Alice", "item": "Book"},
    {"user": "Charlie", "item": "Pen"}
]

def unique_purchases(purchases):

    items_by_user = {}

    for purchase in purchases:

        user = purchase["user"]
        item = purchase["item"]

        if user not in items_by_user:
            items_by_user[user] = set()

        items_by_user[user].add(item)

    result = {}

    for user in items_by_user:
        result[user] = len(items_by_user[user])

    print(result)



    
print(unique_purchases(purchases))