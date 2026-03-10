from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class ScamCheck(Base):
    __tablename__ = "scam_checks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True) # "Safe", "Suspicious", or "Scam"
    category = Column(String)           # "Bank Phishing", etc.
    explanation = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())