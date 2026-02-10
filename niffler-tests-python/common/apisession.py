import json
import logging

from requests import Session, Response
from requests.structures import CaseInsensitiveDict

from common.logging_config import produce_logger

# logger = logging.getLogger(__name__)
logger = produce_logger(__name__)


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        method = response.request.method
        url = response.request.url
        logger.info(f'\n\nREQUEST {method} {url}\n\n'
                    f'REQUEST HEADERS {prettyfy_headers(response.request.headers)}\n\n'
                    f'REQUEST BODY {prettyfy_body(response.request.body)}\n\n'
                    f'RESPONSE HEADERS {prettyfy_headers(response.headers)}\n\n'
                    f'RESPONSE BODY {prettyfy_body(response.content)}\n\n')
        return response

    return wrapper


def prettyfy_headers(headers: CaseInsensitiveDict) -> str:
    if headers:
        return json_dumping(dict(headers))
    else:
        return 'None'


def prettyfy_body(body: bytes) -> str:
    if body:
        try:
            return json_dumping(json.loads(body))
        except:
            return str(body)
    else:
        return 'None'


def json_dumping(dict_to_convert: dict) -> str:
    return json.dumps(dict_to_convert, indent=2, ensure_ascii=False)


class TestSession(Session):
    def __init__(self):
        # def __init__(self, base_url=None):
        super().__init__()
        # self.base_url = base_url

    @allure_request_logger
    def request(self, path='', method='GET', *args, **kwargs):
        joined_url = self.base_url + path
        return super().request(method, joined_url, *args, **kwargs)
