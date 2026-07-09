from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import engine, Base, get_db
from app import repository

Base.metadata.create_all(bind=engine)

app = FastAPI()

class CaseCreate(BaseModel):
    case_number: str
    title: str
    status: str = "open"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/cases")
def create_cases(case: CaseCreate, db: Session = Depends(get_db)):
    return repository.create_case(db, case.case_number, case.title, case.status)

@app.get("/cases")
def list_cases(db: Session = Depends(get_db)):
    return repository.get_cases(db)

