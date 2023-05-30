from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:8999",
    "http://localhost:5173",
    "0.0.0.0:8999"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BalanceRequest(BaseModel):
    IBAN:str
    pin:str

class WithDrawRequest(BaseModel):
    IBAN:str
    amount:int
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



@app.post("/auth")
def gibtoken():
    return {"token":'23314'}


@app.post("/balance")
async def balancePoint(request:BalanceRequest):
    try:
        if request.pin== "223":
            return{"auth":True, "balance":4000}
        else:
            return{"auth":False}
        
    except:
        print("error")
    


@app.post("/withdraw")
async def withdraw(request:WithDrawRequest):
    try:
        print("Withdrawing" + request.amount )
        return {"status":"confirmed"}
    except:
        return {"status": "error"}



