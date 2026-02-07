from pydantic import BaseModel


class Envs(BaseModel):
    frontend_url: str
    gateway_url: str
    spend_db_url: str
    auth_db_url: str
    username: str
    password: str
    auth_url: str
    kafka_bootstrap_servers: str
    userdata_db_url: str
