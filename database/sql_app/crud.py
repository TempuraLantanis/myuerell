# Create, Read, Update and Delete sql query 
from sqlalchemy.orm import Session
from . import models, schemas

def get_account(db:Session, Iban: str):
    return db.query(models.Account).filter(models.Account.Iban == Iban).first()

def get_account_pincode(db: Session, Pincode:str)
    return db.query(models.Account).filter(models.Account.Pincode == Pincode).first()

def get_transaction(db:Session, skip: int = 0. limit: int = 10)
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def create_account(db: Session, account: schemas.AccountCreate):
    fake_Currency = account.Currency + data_Currency
    
    db_account =models.Account(Iban = account.Iban, Currency = fake_Currency)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    fake_FromBank = transaction.FromBank + data_FromBank
    fake_ToBank = transaction.ToBank + data_ToBank
    fake_FromCity = transaction.FromCity + data_FromCity
    fake_ToCity = transaction.ToCity + data_ToCity
    fake_Naam = transaction.Naam + data_Naam
    fake_Currency = transaction.Currency + data_Currency
    fake_Type = transaction.Type + data_Type
    
    db_transactions = models.Transaction(
        Iban = account.Iban
        FromBank = fake_FromBank
        ToBank = fake_ToBank
        FromCity = fake_FromCity
        ToCity = fake_ToCity
        Naam = fake_Naam
        Currency = fake_Currency
        Type = fake_Type
    )
    db.add(db_transactions)
    db.commit()
    db.refresh(db_transactions)
    return db_transactions