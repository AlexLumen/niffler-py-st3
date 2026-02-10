import allure

from models.soap.starships import ListStarships, Starships
from response_errors.response_errors import RESPONSE_BODY_405, RESPONSE_BODY_404


@allure.feature('Starships')
@allure.story('Positive tests')
def test_get_all_starships(api_session):
    response = api_session.request(path='/starships/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
    starships = ListStarships.model_validate(response.json())
    pass


@allure.feature('Starships')
@allure.story('Positive tests')
def test_get_nine_starship(api_session):
    response = api_session.request(path='/starships/9/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
    starship = Starships.model_validate(response.json())
    assert starship.name == 'Death Star'


@allure.feature('Starships')
@allure.story('Positive tests')
def test_get_second_starship(api_session):
    response = api_session.request(path='/starships/2/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
    starship = Starships.model_validate(response.json())
    assert starship.name == 'CR90 corvette'


@allure.feature('Starships')
@allure.story('Positive tests')
def test_search_starship(api_session):
    response = api_session.request(path='/starships/12/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
    starship = Starships.model_validate(response.json())
    assert starship.name == 'X-wing'


@allure.feature('Starships')
@allure.story('Negative tests')
def test_404(api_session):
    response = api_session.request(path='/wrong/')
    assert response.status_code == 404
    assert response.headers.get('content-type') == 'text/html'


@allure.feature('Starships')
@allure.story('Negative tests')
def test_405(api_session):
    response = api_session.request(path='/starships/', method='POST')
    assert response.status_code == 405
    assert response.json() == RESPONSE_BODY_405


@allure.feature('Starships')
@allure.story('Negative tests')
def test_wrong_qwery(api_session):
    response = api_session.request(path='/starships/asdgf/')
    assert response.status_code == 404
    assert response.json() == RESPONSE_BODY_404
