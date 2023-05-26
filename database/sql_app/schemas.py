from typing import Optional, List, Union
from pydantic import BaseModel

# to support Creation and update API
class CreateAndUpdateAccount(BaseModel):
Naam: str
Pincode: str
Currency: str
Status: str

class Account(CreateAndUpdateAccount):
    Iban: str
    
    class Config:
        orm_mode = True

class CreateAndUpdateTransation(BaseModel):    
    Iban: str
    FromBank: str
    ToBank: str
    FromCity: str
    ToCity: str
    Naam: str
    Currency: str
    Type: str

class Transaction(CreateAndUpdateTransation):
    ID = int
    
    class Config:
        orm_mode = True
        
class CreateAndUpdateBankcode(BaseModel):
    Code: str
    Name: str
    City: str
    Land: str
    IPv4Address: str
    
class BankCode(CreateAndUpdateBankcode):
    ID = str
    
    class Config:
        orm_mode = True
        
class paginatedAccountInfo(BaseModel):
    limit: int
    offset: int
    data: List[Account]
        