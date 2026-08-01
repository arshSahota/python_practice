response = {
    "userId": 101,
    "name": "John",
    "email": "john@test.com",
    "active": True
}

def validate_response(response):

    return(
        isinstance(response.get("userId"), int) and
        response.get("name", "") != "" and
        "@" in response.get("email", "") and
        isinstance(response.get("active"), bool)
    )

print(validate_response(response))