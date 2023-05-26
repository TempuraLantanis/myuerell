from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# Create the database models

class Account(Base):
    __tablename__ = "account"
    
    Iban =      Colum(String, primary_key = True, index = True)
    Naam =      Colum(String, index = True)
    Pincode =   Colum(String, index = True)
    Currency =  Colum(String, index = True)
    Status =    Colum(String, index = True)
    
    transaction = relationship("transaction", back_populates = "account")
    
class Transaction(Base):
    __tablename__ = "transaction"
    
    ID =        Colum(String, primary_key = True, index = True)
    Iban =      Colum(String, ForiegnKey("account.Iban"), index = True)
    FromBank =  Colum(String, index = True)
    ToBank =    Colum(String, index = True)
    FromCity =  Colum(String, index = True)
    ToCity =    Colum(String, index = True)
    Naam =      Colum(String, index = True)
    Currency =  Colum(String, index = True)
    Type =      Colum(String, index = True)
    
    owner = relationship("Account", back_populates = "transaction")
    
class BankCode(Base):
    __tablename__ = "bankcode"
    
    ID =            Colum(String,primary_key = True , index = True)
    Code =          Colum(String, index = True)
    Name =          Colum(String, index = True)
    City =          Colum(String, index = True)
    Land =          Colum(String, index = True)
    IPv4Address =   Colum(String, index = True)