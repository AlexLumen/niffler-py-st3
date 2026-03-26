import allure
import grpc
import pytest

from internal.pb.niffler_currency_pb2 import CalculateRequest, CurrencyValues
from internal.pb.niffler_currency_pb2_pbreflect import NifflerCurrencyServiceClient


@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация Евро в рубли')
def test_calculate_rate(grpc_client: NifflerCurrencyServiceClient) -> None:
    response = grpc_client.calculate_rate(
        request=CalculateRequest(
            spendCurrency=CurrencyValues.EUR,
            desiredCurrency=CurrencyValues.RUB,
            amount=66.0
        )
    )
    assert response.calculatedAmount == 4752.0


@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация без параметра desired_currency')
def test_calculate_rate_without_desired_currency(grpc_client: NifflerCurrencyServiceClient) -> None:
    try:
        grpc_client.calculate_rate(
            request=CalculateRequest(
                spendCurrency=CurrencyValues.EUR,
                amount=100.0
            )
        )
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.UNKNOWN
        assert e.details() == "Application error processing RPC"


@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация без параметра amount')
def test_calculate_rate_without_amount(grpc_client: NifflerCurrencyServiceClient, ) -> None:
    try:
        grpc_client.calculate_rate(
            request=CalculateRequest(
                spendCurrency=CurrencyValues.EUR,
                desiredCurrency=CurrencyValues.RUB
            )
        )
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.UNKNOWN
        assert e.details() == "Application error processing RPC"


@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация без параметра spendCurrency')
def test_calculate_rate_without_spend_currency(grpc_client: NifflerCurrencyServiceClient, ) -> None:
    try:
        grpc_client.calculate_rate(
            request=CalculateRequest(
                desiredCurrency=CurrencyValues.RUB,
                amount=100.0
            )
        )
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.UNKNOWN
        assert e.details() == "Application error processing RPC"


@pytest.mark.parametrize("spend, spend_currency, desired_currency, expected_result", [
    (100.0, CurrencyValues.USD, CurrencyValues.RUB, 6666.67),
    (100.0, CurrencyValues.RUB, CurrencyValues.USD, 1.5),
    (100.0, CurrencyValues.USD, CurrencyValues.USD, 100.0),
    (44.4, CurrencyValues.KZT, CurrencyValues.USD, 0.09),
    (0.09, CurrencyValues.USD, CurrencyValues.KZT, 42.86),
])
@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация долларов в разные валюты и обратно')
def test_currency_conversions_usd(
        grpc_client: NifflerCurrencyServiceClient,
        spend: float,
        spend_currency: CurrencyValues,
        desired_currency: CurrencyValues,
        expected_result: float
):
    response = grpc_client.calculate_rate(
        request=CalculateRequest(
            spendCurrency=spend_currency,
            desiredCurrency=desired_currency,
            amount=spend
        )
    )
    assert response.calculatedAmount == expected_result, f"Expected {expected_result}"


@pytest.mark.parametrize("spend, spend_currency, desired_currency, expected_result", [
    (150.0, CurrencyValues.EUR, CurrencyValues.USD, 162.0),
    (50, CurrencyValues.USD, CurrencyValues.EUR, 46.3),
    (66.0, CurrencyValues.EUR, CurrencyValues.RUB, 4752.0),
    (100.0, CurrencyValues.RUB, CurrencyValues.EUR, 1.39),
    (77.7, CurrencyValues.EUR, CurrencyValues.KZT, 39960.0),
    (55578.92, CurrencyValues.KZT, CurrencyValues.EUR, 108.07),
])
@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация Евро в разные валюты и обратно')
def test_currency_conversions_eur(
        grpc_client: NifflerCurrencyServiceClient,
        spend: float,
        spend_currency: CurrencyValues,
        desired_currency: CurrencyValues,
        expected_result: float
):
    response = grpc_client.calculate_rate(
        request=CalculateRequest(
            spendCurrency=spend_currency,
            desiredCurrency=desired_currency,
            amount=spend
        )
    )
    assert response.calculatedAmount == expected_result, f"Expected {expected_result}"


@pytest.mark.parametrize("spend, spend_currency, desired_currency, expected_result", [
    (55578.00, CurrencyValues.KZT, CurrencyValues.RUB, 7780.92),
    (5000.0, CurrencyValues.RUB, CurrencyValues.KZT, 35714.29)
])
@allure.epic("grpc")
@allure.feature("Курсы валют")
@allure.title('Конвертация Тенге в разные валюты и обратно')
def test_currency_conversions_kzt(
        grpc_client: NifflerCurrencyServiceClient,
        spend: float,
        spend_currency: CurrencyValues,
        desired_currency: CurrencyValues,
        expected_result: float
):
    response = grpc_client.calculate_rate(
        request=CalculateRequest(
            spendCurrency=spend_currency,
            desiredCurrency=desired_currency,
            amount=spend
        )
    )
    assert response.calculatedAmount == expected_result, f"Expected {expected_result}"
