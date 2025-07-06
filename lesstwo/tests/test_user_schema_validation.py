import allure
import requests

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from lesstwo.utils.logger import logger
from lesstwo.schemas.user_schema import user_schema
from lesstwo.schemas.user_list_schema import user_list_schema

@allure.feature("User validation")
@allure.story("User chema validation")
def test_user_schema_validation(client):
    with allure.step("Create request"):
        response = client.get_user(id=2)

        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        if response.status_code != 200:
            allure.attach(response.text, "Invalid statuse code")

        assert response.status_code == 200

    with allure.step("Check response"):
        data = response.json()
        try:
            validate(instance=data, schema=user_schema)
        except ValidationError as e:
            allure.attach(str(e), name="Validation Error",
                          attachment_type=allure.attachment_type.TEXT)
            assert False, f"JSON Schema validation failed {e}"

@allure.feature("Users list validation")
@allure.story("")
def test_user_list_schema(client):
    with allure.step("Create request"):
        response = client.get_users(page=2)

        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        if response.status_code != 200:
            allure.attach(response.text, "Invalid statuse code")

        assert response.status_code == 200

    with allure.step("Check response"):
        data = response.json()

        try:
            validate(instance=data, schema=user_list_schema)
        except ValidationError as e:
            allure.attach(str(e), name="Validation Error",
                          attachment_type=allure.attachment_type.TEXT)
            assert False, f"JSON Schema validation failed {e}"
