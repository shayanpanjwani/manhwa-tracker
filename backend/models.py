from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from database import Base

class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    current_chapter =  Column(Integer, nullable=False)
    total_chapters_available = Column(Integer, nullable=False)
    last_read_date = Column(DateTime, default=datetime.now(timezone.utc))
    date_added = Column(DateTime, default=datetime.now(timezone.utc))
    rating = Column(Integer, nullable=True)
    aggregator_url = Column(String, nullable=True)