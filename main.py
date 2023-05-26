from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from sqlalchemy import create_engine


connection_string = "mysql+mysqlconnector://user:password@145.24.222.57:3310/testDB"
engine = create_engine(connection_string,echo=True)



app = FastAPI()


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



