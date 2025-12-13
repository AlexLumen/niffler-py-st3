from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str
    enabled: bool
    account_non_expired: bool
    account_non_locked: bool
    credentials_non_expired: bool
