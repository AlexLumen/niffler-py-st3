from sqlmodel import SQLModel, Field


class Authority(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    user_id: str
    authority: bool
