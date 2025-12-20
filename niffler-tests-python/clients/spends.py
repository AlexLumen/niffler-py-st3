from urllib.parse import urljoin

import allure
import requests
from requests import Response
from allure_commons.types import AttachmentType
from requests_toolbelt.utils.dump import dump_response


class SpendsHttpClient:
    session: requests.Session
    base_url: str

    def __init__(self, base_url: str, token: str, ):
        self.base_url = base_url
        self.session = requests.session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        self.session.hooks["response"].append(self.attach_response)

    @staticmethod
    def attach_response(response: Response, *args, **kwargs):
        attachment_name = response.request.method + " " + response.request.url
        allure.attach(dump_response(response), attachment_name, attachment_type=AttachmentType.TEXT)

    def get_categories(self):
        response = self.session.get(urljoin(self.base_url, "/api/categories/all"))
        response.raise_for_status()
        return response.json()

    def add_category(self, name: str):
        response = self.session.post(urljoin(self.base_url, "/api/categories/add"), json={
            "name": name
        })
        response.raise_for_status()
        return response.json()

    def add_spends(self, body):
        url = urljoin(self.base_url, "/api/spends/add")
        response = self.session.post(url, json=body)
        response.raise_for_status()
        return response.json()

    def remove_spends(self, ids: str):
        url = urljoin(self.base_url, "/api/spends/remove")
        response = self.session.delete(url, params={"ids": ids})
        response.raise_for_status()

    def update_category(self, body):
        url = urljoin(self.base_url, "/api/categories/update")
        response = self.session.patch(url, json=body)
        response.raise_for_status()
        return response.json()
