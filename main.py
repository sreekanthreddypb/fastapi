from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Swami Vivekananda"}

@app.get("/itemname/{itemname}")
async def root2(item):
    return {'ItemName': item}

@app.get("/itemid/{item_id}")
async def root3(item_id : int):
    return {'ItemId': item_id}

#oreder is important, this api needs to first
@app.get('/users/me')
async def read_user_me():
    return {'user':"sreekanthreddy"}
#oreder is important, this api needs to last
@app.get('/users/{username}')
async def read_user(username):
    return {'user': username}

class ModelName(str, Enum):
    rama = "rama"
    shiva = "shiva"
    creator = "Bramha"

@app.get('/models/{model_name}')
async def get_god_details(model_name: ModelName):
    if model_name is ModelName.rama:
        return {'model_name': model_name, "msg":"Follow Rama"}

    elif model_name.value == "shiva":
        return {'model_name': model_name, 'msg': "Follow Completeness"}
    return {"model_name":model_name, "msg": "follow Creator"}

