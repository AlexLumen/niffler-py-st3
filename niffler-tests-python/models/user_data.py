from pydantic import BaseModel


class UserData(BaseModel):
    username: str
    password: str
    submit_password: str
    first_name: str
