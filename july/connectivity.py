devices = [
    {
        "id": "D001",
        "online": True
    },
    {
        "id": "D002",
        "online": False
    },
    {
        "id": "D003",
        "online": True
    },
    {
        "id": "D004",
        "online": False
    }
]

def check_connectivity(devices):

    online = []
    offline = []

    for device in devices:

        id = device["id"]
        status = device["online"]

        if status == True:
            online.append(id)

        else:
            offline.append(id)

    return{
        "online": online,
        "offline": offline
    }

print(check_connectivity(devices))