import requests


def get_weather(city):
    """Получает погоду для города и возвращает температуру"""
    url = f"https://api.weather.com/v1/current?city={city}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не удалось получить погоду")

    data = response.json()      # десериализуем json-текст от сервера в пайтон-словарь
    return data["temperature"]  # достаем из словаря значение по ключу temperature и возвращаем его
