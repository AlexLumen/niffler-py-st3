from pydantic import BaseModel
from sqlalchemy import MetaData
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    metadata = MetaData()
    id: str = Field(default=None, primary_key=True)
    username: str
    currency: str
    firstname: str
    surname: str
    photo: str | None = None
    photo_small: str | None = None
    __table_args__ = {"extend_existing": True}


class UserName(BaseModel):
    username: str
