import allure
import requests
import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from lesstwo.schemas.user_schema import user_schema
from lesstwo.schemas.user_list_schema import user_list_schema
from lesstwo.tests.get_requests import BASE_URL

@allure.feature("User validation")
@allure.story("User chema validation")
def test_user_schema_validation():
    with allure.step("Create request"):
        response = requests.get(f"{BASE_URL}users/2")

        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response body: {response.text}")

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
def test_user_list_schema():
    with allure.step("Create request"):
        response = requests.get(f"{BASE_URL}users?page=2")

        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response body: {response.text}")

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
