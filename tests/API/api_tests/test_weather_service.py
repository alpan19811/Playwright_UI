import pytest
from unittest.mock import patch, Mock
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from services.weather_service import get_weather


@patch("weather_service.requests.get")                    # Декоратор patch говорит Python: "Пока выполняется этот тест, перехватывай любые вызовы requests.get внутри модуля weather_service и заменяй их на фейковый объект".
def test_get_weather_success(mock_get):
    mock_response = Mock()                                # Создаём пустой фейковый объект, который будет имитировать ответ от сервера (response).
    mock_response.status_code = 200                       # Настраиваем фейк: если функция проверит response.status_code, ей вернётся 200.
    mock_response.json.return_value = {"temperature": 25} #  Настраиваем фейк: если функция вызовет response.json(), ей вернётся словарь {"temperature": 25}.
    mock_get.return_value = mock_response                 # Связываем всё вместе: когда функция внутри себя вызовет requests.get(url), ей вернётся наш настроенный mock_response.


    temp = get_weather("Moscow")

    assert temp == 25

    mock_get.assert_called_once_with("https://api.weather.com/v1/current?city=Moscow")


@patch("weather_service.requests.get")
def test_get_weather_error(mock_get):
    # Настраиваем ответ с ошибкой
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Проверяем, что функция выбрасывает исключение
    with pytest.raises(Exception, match="Не удалось получить погоду"): # Контекстный менеджер pytest.raises ожидает, что внутри блока with будет выброшено исключение Exception. Параметр match проверяет, что текст ошибки содержит указанную подстроку.
        get_weather("UnknownCity")