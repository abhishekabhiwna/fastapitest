from fastapi import FastAPI
import schemas

app = FastAPI()

fakedata = {
    1:{'task':'clean car'},
    2:{'task':'clean home'},
    3:{'task':'clean bike'},
}
@app.get("/")
def getitems():
    return fakedata

@app.get("/{id}")
def getitem(id:int):
    return fakedata[id]

@app.post('/')
def postitem(item:schemas.Item):
    newid = len(fakedata.keys()) + 1
    fakedata[newid] = {'task':item.task}
    return fakedata

