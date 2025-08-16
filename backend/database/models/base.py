from symtable import Class

from sqlalchemy import Column, DateTime, func

class TimeStampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
