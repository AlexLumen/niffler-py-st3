import logging

import pytest

from common.apisession import TestSession
from common.project import config


@pytest.fixture(scope='session')
def api_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    session.headers['api-key'] = config.api_key
    return session


@pytest.fixture(scope='session')
def api_wookie_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    session.params = {'format': 'wookiee'}

    return session


@pytest.fixture(scope='function')
def api_destruction_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})

    return session


@pytest.fixture(scope='module')
def api_module_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})

    return session


@pytest.fixture(scope='module')
def soap_session():
    session = TestSession()
    session.base_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'
    session.headers.update({'Content-Type': 'application/soap+xml'})

    return session
