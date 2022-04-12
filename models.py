from datetime import datetime
from database import Base
from sqlalchemy import Column,String,Boolean,Integer,DateTime


class DbAttendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(DateTime)



