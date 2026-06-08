from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv
 
load_dotenv()
 
DATABASE_URL = os.getenv(
    'DATABASE_URL'
    # 'postgresql://postgres:password@localhost:5432/road_damage'
)
 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
 
 
class Detection(Base):
    __tablename__ = 'detections'
 
    id          = Column(Integer, primary_key=True, index=True)
    image_name  = Column(String(255))
    latitude    = Column(Float, nullable=True)
    longitude   = Column(Float, nullable=True)
    class_name  = Column(String(50))
    confidence  = Column(Float)
    severity    = Column(String(20))
    area_pct    = Column(Float)
    timestamp   = Column(DateTime, default=datetime.utcnow)
    image_path  = Column(Text, nullable=True)
 
 
def create_tables():
    Base.metadata.create_all(bind=engine)
 
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()