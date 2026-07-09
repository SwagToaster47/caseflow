from sqlalchemy.orm import Session
from app import models

def create_case(db: Session, case_number: str, title: str, status: str = "open"):
    case = models.Case(case_number=case_number, title=title, status=status)
    db.add(case)
    db.commit()
    db.refresh(case)
    return case

def get_cases(db: Session):
    return db.query(models.Case).all()

