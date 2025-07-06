import allure
import requests
import logging

from lesstwo.tests.get_requests import BASE_URL

@allure.feature("Reqres API: POST")
@allure.story("Создание юзера")
def test_create_user():
    with allure.step("Формируем данные для нового юзера"):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

    with allure.step("Отправялем запрос на создание юзера"):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        response = requests.post(f"{BASE_URL}users", json=payload, headers=headers)
        logging.info(f"Create user: Status of response {response.status_code}")
        assert response.status_code == 201

    with allure.step("Проверка ответа"):
        data = response.json()
        assert data["name"] == "morpheus"
        assert "id" in data
        logging.info(f"Crate user: Response\n {data}")

@allure.feature("Reqres API: POST")
@allure.story("Регистрация")
def test_registration():
    with allure.step("Формируем payload"):
        payload = {
            "email":"eve.holt@reqres.in",
            "password":"pistol"
        }
        headers = {
            "x-api-key": "reqres-free-v1"
        }

    with allure.step("Отправка запроса"):
        response = requests.post(f"{BASE_URL}register", json=payload, headers=headers)

        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response body: {response.text}")

        if response.status_code != 200:
            allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 200

    with allure.step("Проверка ответа"):
        data = response.json()
        assert "token" in data
        assert "id" in data
