from dataclasses import dataclass


@dataclass
class Config:
    api_key: str
    url: str


config = Config(
    api_key='super_secret_api_key',
    url='https://swapi.dev/api/films'
)
