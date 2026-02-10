import allure
from xmlschema import XMLSchemaChildrenValidationError

from schemas.templates.read_templates import country_iso_code_xml, xsd_response, country_name_xml
from utils.check_result_operation import check_result_operation


@allure.feature('SOAP')
def test_country_name_service(soap_session):
    response = soap_session.request(method='POST', data=country_iso_code_xml('IT'))
    assert response.status_code == 200

    try:
        xsd_response('CountryNameResponse').validate(response.text)
    except XMLSchemaChildrenValidationError as xsd_e:
        raise AssertionError(xsd_e)

    assert check_result_operation(response.text, 'Italy')


@allure.feature('SOAP')
def test_country_iso_service(soap_session):
    response = soap_session.request(method='POST', data=country_name_xml('Italy'))
    assert response.status_code == 200

    try:
        xsd_response('CountryISOCodeResponse').validate(response.text)
    except XMLSchemaChildrenValidationError as xsd_e:
        raise AssertionError(xsd_e)

    assert check_result_operation(response.text, 'IT')
