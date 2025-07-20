import allure
import pytest
from lesstwo.utils.logger import logger

@allure.feature("Login test")
@allure.story("Positive login")
@pytest.mark.parametrize("email, password", [
    ("eve.holt@reqres.in", "cityslicka"),
])
def test_successful_login(client, email, password):
    response = client.login(email=email, password=password)
    logger.info(f"Response: {response.json()}")

    assert response.status_code == 200
    assert "token" in response.json()

@allure.story("Negative login")
@pytest.mark.parametrize("email, password", [
    ("peter@klaven", None),
    ("", "somepass"),
    ("invalid@", "123"),
])
def test_login_failure(client, email, password):
    response = client.login(email=email, password=password)
    logger.info(f"Negative response: {response.status_code}")
    assert response.status_code == 400
    assert "error" in response.json()