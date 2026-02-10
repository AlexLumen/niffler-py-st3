import allure

from models.soap.people import People
from response_errors.response_errors import RESPONSE_BODY_405, RESPONSE_BODY_404


@allure.feature('People')
@allure.story('Positive tests')
def test_get_all_people(api_session):
    response = api_session.request(path='/people/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'



@allure.feature('People')
@allure.story('Positive tests')
def test_get_first_people(api_session):
    response = api_session.request(path='/people/1/')

    assert response.status_code == 200
    people = People.model_validate(response.json())
    assert people.name == 'Luke Skywalker'


@allure.feature('People')
@allure.story('Positive tests')
def test_get_second_people(api_session):
    response = api_session.request(path='/people/2/')
    assert response.status_code == 200
    people = People.model_validate(response.json())
    assert people.name == 'C-3PO'


@allure.feature('People')
@allure.story('Positive tests')
def test_get_without_header_user_agent(api_session):
    api_session.headers.pop('user-agent')
    response = api_session.request(path='/people/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'


@allure.feature('People')
@allure.story('Positive tests')
def test_search_people(api_session):
    response = api_session.request(path='/people/10/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
    people = People.model_validate(response.json())
    assert people.name == 'Obi-Wan Kenobi'


@allure.feature('People')
@allure.story('Negative tests')
def test_404(api_session):
    response = api_session.request(path='/wrong/')
    assert response.status_code == 404
    assert response.headers.get('content-type') == 'text/html'


@allure.feature('People')
@allure.story('Negative tests')
def test_405(api_session):
    response = api_session.request(path='/people/', method='POST')
    assert response.status_code == 405
    assert response.json() == RESPONSE_BODY_405


@allure.feature('People')
@allure.story('Negative tests')
def test_wrong_qwery(api_session):
    response = api_session.request(path='/people/asdgf/')
    assert response.status_code == 404
    assert response.json() == RESPONSE_BODY_404
