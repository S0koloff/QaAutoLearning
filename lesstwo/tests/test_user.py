import allure
from lesstwo.utils.logger import logger

@allure.feature("User actions")
@allure.story("Delete user")
def test_delete_user(client):
    response = client.delete_user(2)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 204