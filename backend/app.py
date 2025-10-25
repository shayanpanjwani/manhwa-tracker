from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Manhwa Tracker API is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/series", response_model=List[schemas.Series])
def get_all_series(db: Session = Depends(get_db)):
    series = db.query(models.Series).order_by(models.Series.last_read_date.desc()).all()
    return series

@app.post("/api/series", response_model=schemas.Series)
def create_series(series: schemas.SeriesCreate, db: Session = Depends(get_db)):
    db_series = models.Series(**series.model_dump())
    db.add(db_series)
    db.commit()
    db.refresh(db_series)
    return db_series
