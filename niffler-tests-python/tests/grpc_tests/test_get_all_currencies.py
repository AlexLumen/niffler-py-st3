import allure
from internal.pb.niffler_currency_pb2_pbreflect import NifflerCurrencyServiceClient
from google.protobuf import empty_pb2
from internal.pb.niffler_currency_pb2 import CurrencyValues


@allure.feature("Курсы валют")
@allure.title('Получить все курсы валют')
def test_get_all_currencies(grpc_client: NifflerCurrencyServiceClient) -> None:
    response = grpc_client.get_all_currencies(empty_pb2.Empty())
    assert len(response.allCurrencies) == 4
