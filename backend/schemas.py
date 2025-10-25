from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SeriesBase(BaseModel):
    title: str
    current_chapter: int
    total_chapters_available: int
    rating: Optional[int] = None
    aggregator_url: Optional[str] = None

class SeriesCreate(SeriesBase):
    pass

class Series(SeriesBase):
    id: int
    last_read_date: datetime
    date_added: datetime

    class Config:
        from_attributes = True