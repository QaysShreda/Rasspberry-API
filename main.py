from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import db_attendance
import models
from database import get_db, engine
from db_attendance import reg_attendance
from schemas import AttindanceBase
from deta import Deta

app = FastAPI(
title="Raspberry Pi API (Think deep Group)",
tags=['Raspberry pi Group']
)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.post('/')
def set_attendance(request:AttindanceBase,db:Session = Depends(get_db)):
    return reg_attendance(db,request)

@app.get('/all')
def get_all(db:Session = Depends(get_db)):
    return db_attendance.get_all(db)


@app.delete('/delete/{id}')
def delete(id:int,db:Session= Depends(get_db)):
    return db_attendance.delete(db,id)


models.Base.metadata.create_all(engine)