from fastapi import HTTPException,status,Response
from sqlalchemy.orm.session import Session

from models import DbAttendance
from schemas import  AttindanceBase


def reg_attendance(db:Session,request:AttindanceBase):
    new_attendance = DbAttendance(
        name = request.name,
        date = request.date
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

def get_all(db:Session):
    return db.query(DbAttendance).all()

def delete(db:Session,id:int):
    attebdance = db.query(DbAttendance).filter(DbAttendance.id == id).first()
    if not attebdance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with id {id} not found')

    db.delete(attebdance)
    db.commit()
    return 'ok'