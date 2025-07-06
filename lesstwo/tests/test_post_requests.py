import allure
import requests

from lesstwo.utils.logger import logger

@allure.feature("Reqres API: POST")
@allure.story("Создание юзера")
def test_create_user(client):
    with allure.step("Формируем данные для нового юзера"):
        name = "morpheus"
        job = "leader"

    with allure.step("Отправялем запрос на создание юзера"):
        response = client.create_user(name, job)
        logger.info(f"Create user: Status of response {response.status_code}")
        assert response.status_code == 201

    with allure.step("Проверка ответа"):
        data = response.json()
        assert data["name"] == "morpheus"
        assert "id" in data
        logger.info(f"Crate user: Response\n {data}")

@allure.feature("Reqres API: POST")
@allure.story("Регистрация")
def test_registration(client):
    with allure.step("Формируем payload"):
        email = "eve.holt@reqres.in"
        password = "pistol"

    with allure.step("Отправка запроса"):
        response = client.register_user(email, password)
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        if response.status_code != 200:
            allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 201

    with allure.step("Проверка ответа"):
        data = response.json()
        assert "token" in data
        assert "id" in data
