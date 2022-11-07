#colocar test_ é obrigatórios pois ele lê os arquivos de teste, precisa começar ou terminar com test
import datetime
from tkinter import EXCEPTION
import requests
from mercado_bitcoin.apis import DaySummaryApi, MercadoBitcoinApi, TradesApi
import pytest

from unittest.mock import patch, mock_open


class TestDaySumarryApi:

    @pytest.mark.parametrize(
        "coin, date, expected",
        [
            ("BTC",datetime.date(2022,6,20),"https://www.mercadobitcoin.net/api/BTC/day-summary/2022/6/20"),
            ("ETH",datetime.date(2022,6,20),"https://www.mercadobitcoin.net/api/ETH/day-summary/2022/6/20"),
            ("ETH",datetime.date(2022,1,1),"https://www.mercadobitcoin.net/api/ETH/day-summary/2022/1/1")
        ]
    )
    def test_get_endpoint(self, coin, date, expected):
        api = DaySummaryApi(coin=coin)
        actual = api._get_endpoint(date=date)
        assert  actual == expected
    
    #cada questão deverá ser apenas um assert
    
# def test_get_endpoint_api_ETH():
#     date = datetime.date(2022,6,20)
#     api = DaySummaryApi(coin='ETH')
#     actual = api._get_endpoint(date=date)
#     expected = "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/6/20"
#     assert  actual == expected
    
    #cada questão deverá ser apenas um assert
    
    
class TestTradesApi:

    @pytest.mark.parametrize(
        "date_from, date_to, coin, expected",
        [
            (datetime.datetime(2022,1,1), datetime.datetime(2022, 1, 2), "TEST",
             "https://www.mercadobitcoin.net/api/TEST/trades/1641006000/1641092400"),
            (datetime.datetime(2022,1,1), None, "TEST",
             "https://www.mercadobitcoin.net/api/TEST/trades/1641006000"),
            (None, datetime.datetime(2022, 1, 2), "TEST",
             "https://www.mercadobitcoin.net/api/TEST/trades"),
            (None, None, "TEST",
             "https://www.mercadobitcoin.net/api/TEST/trades"),
            
        ]
    )
    def test_get_endpoint(self, date_from, date_to, coin, expected):
        actual = TradesApi(coin=coin)._get_endpoint(date_from=date_from, date_to=date_to)
        assert  actual == expected
        
    def test_get_endpoint_date_from_greater_than_date_to(self):
        with pytest.raises(RuntimeError):
            TradesApi(coin='TEST')._get_endpoint(
                date_from=datetime.datetime(2022, 1, 20),
                date_to=datetime.datetime(2022, 1, 1)
            )
        
    @pytest.mark.parametrize(
        "date, expected",

        [
           (datetime.datetime(2022,1, 1), 1641006000),
           (datetime.datetime(2022,1, 1), 1641006000),
           (datetime.datetime(2022, 6, 12, 0 , 0, 5), 1655002805),
           (datetime.datetime(2022, 12, 15), 1671073200)
           
        ]
    )   
    def test_get_unix_epoch(self, date, expected):
        actual = TradesApi(coin='TEST')._get_unix_epoch(date)
        assert actual==expected
        
        
@pytest.fixture()
@patch("mercado_bitcoin.apis.MercadoBitcoinApi.__abstractmethods__", set())
def fixture_mercado_bitcoin_api():
    return MercadoBitcoinApi(
        coin="test"
    )        

def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.status_code = status_code
            self.json_data = json_data
            
        def json(self):
            return self.json_data
        
        
        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception
        
    if args[0] =="valid_endpoint":
        return MockResponse(json_data={"foo":"bar"}, status_code = 200)
    else:
        return MockResponse(json_data=None, status_code = 404)
             


class TestMercadoBitcoinApi:
    
    @patch("requests.get")
    @patch("mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="valid_endpoint")
    def test_get_data_requests_is_called(self, mock_get_endpoint, mock_requests,fixture_mercado_bitcoin_api):
        fixture_mercado_bitcoin_api.get_data()
        mock_requests.assert_called_once_with('valid_endpoint')
        
    @patch("requests.get", side_effect=mocked_requests_get)
    @patch("mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="valid_endpoint")    
    def test_get_data_with_valid_endpoint(self, mock_get_endpoint, mock_requests, fixture_mercado_bitcoin_api):
        actual = fixture_mercado_bitcoin_api.get_data()
        expected = {"foo": "bar"}
        assert actual == expected
    
    @patch("requests.get", side_effect=mocked_requests_get)
    @patch("mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="invalid_endpoint")    
    def test_get_data_with_invalid_endpoint(self, mock_get_endpoint, mock_requests, fixture_mercado_bitcoin_api):
        with pytest.raises(Exception):
            fixture_mercado_bitcoin_api.get_data()
            