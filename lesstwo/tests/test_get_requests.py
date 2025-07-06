import requests
import allure
from lesstwo.utils.logger import logger

@allure.feature("Reqres API: GET")
@allure.story("Список пользователей")
def test_get_users_list(client):
    with allure.step("Отправляем Get-запрос"):
        response = client.get_users(page=2)
        logger.info(f"Users list\nStatus code: {response.status_code}")
        assert  response.status_code == 200

    with allure.step("Проверка ответа"):
        data = response.json()
        logger.info(f"Users list\nResponse: {data}")
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0

@allure.feature("Reqres API")
@allure.story("Один юзер")
def test_get_single_user(client):
    with allure.step("Отправляем запрос"):
        response = client.get_user(id=2)
        logger.info(f"Status code: {response.status_code}")
        assert  response.status_code == 200

    with allure.step("Проверка ответа"):
        data = response.json()
        logger.info(f"Response: {data}")
        assert "data" in data
        assert data["data"]["id"] == 2
        assert "email" in data["data"]