from urllib.parse import urljoin

import allure
import requests
from requests import Response
from allure_commons.types import AttachmentType
from requests_toolbelt.utils.dump import dump_response

from models.category import Category
from models.config import Envs
from models.spend import Spend, SpendAdd
from utils.sessions import BaseSession


class SpendsHttpClient:
    session: requests.Session
    base_url: str

    def __init__(self, envs, token: str):
        self.base_url = envs.gateway_url
        self.session = BaseSession(base_url=self.base_url)
        self.session.headers.update({
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

    def get_categories(self) -> list[Category]:
        response = self.session.get("/api/categories/all")
        return [Category.model_validate(item) for item in response.json()]

    def add_category(self, name: str) -> Category:
        response = self.session.post("/api/categories/add", json={
            "name": name
        })
        return Category.model_validate(response.json())

    def get_spends(self) -> list[Spend]:
        response = self.session.get("/api/spends/all")
        return [Spend.model_validate(item) for item in response.json()]

    def add_spends(self, spend: SpendAdd) -> Spend:
        response = self.session.post("/api/spends/add", json=spend.model_dump())
        return Spend.model_validate(response.json())

    def remove_spends(self, ids: list[str]):
        response = self.session.delete("/api/spends/remove", params={"ids": ids})
        return response

    def update_category(self, body):
        response = self.session.patch("/api/categories/update", json=body)
        response.raise_for_status()
        return response.json()
