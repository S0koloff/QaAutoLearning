import pytest
import logging
from lesstwo.utils.faker_data import generate_user_name_job_data

users = [generate_user_name_job_data() for _ in range(2)]
invalid_user = ("", "Invalid Job", 400)

test_data = [ *[(user["name"], user["job"], 201) for user in users],
                invalid_user]

@pytest.mark.parametrize("name, job, expected_status", test_data)
def test_usercreate(client, name, job, expected_status):
    logging.info(f"Создааем юзера\n Name: {name} Job: {job}\n Ожидаемый статус: {expected_status}")
    request = client.create_user(name, job)
    assert request.status_code == expected_status