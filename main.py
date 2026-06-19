from fastapi import FastAPI, HTTPException

app = FastAPI()

albums = [
    {
        "id": 1,
        "title": "Blue Train",
        'artist': "John Coltrane",
        "price": 56.99
    },
    {
        "id": 2,
        "title": "Jeru",
        "artist": "Gerry Mulligan",
        "price": 17.99
    },
    {
        "id": 3,
        "title": "Sarah Vaughan and Clifford Brown",
        "artist": "Sarah Vaughan",
        "price": 39.99
    },
]


@app.get('/albums')
async def getAlbums():
    return albums


@app.get('/albums/{id}')
async def getAlbumById(id: int):
    for i in albums:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail="Product not found")
