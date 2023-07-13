import requests as req


def getOneUser(id):
    url = "https://jsonplaceholder.typicode.com/users/"
    response = req.get(url)
    return response.json()[id]

getOneUser(id=1)