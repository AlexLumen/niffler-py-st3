from datetime import datetime

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Spend(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    amount: float
    description: str
    category_id: str
    spend_date: datetime
    currency: str
    username: str
