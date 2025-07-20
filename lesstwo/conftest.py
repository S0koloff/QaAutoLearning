import logging
import pytest
import shutil
import os

from lesstwo.client.reqres_client import ReqresClient


def pytest_configure(config):
    logging.basicConfig(
        filename='../test_log.log',
        level=logging.INFO,
        format ='%(asctime)s [%(levelname)s] %(message)s',
        filemode='w'
    )

def pytest_sessionstart(session):
    """Вызывается перед запуском тестов."""
    dir_path = "../allure-results"
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)  # удаляем папку вместе с содержимым
    os.makedirs(dir_path)  # создаём папку заново

@pytest.fixture(scope="session")
def client():
    return ReqresClient()