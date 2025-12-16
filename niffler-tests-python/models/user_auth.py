from pydantic import BaseModel


class UserAuth(BaseModel):
    user_name: str
    password: str
