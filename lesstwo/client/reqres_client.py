import requests

class ReqresClient:
    BASE_URL = "https://reqres.in/api/"

    def get_users(self, page=1):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        return requests.get(f"{self.BASE_URL}users", params={"page" : page}, headers=headers)

    def get_user(self, id=2):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        return requests.get(f"{self.BASE_URL}users/{id}", headers=headers)

    def create_user(self, name: str, job: str):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        payload = {
            "name" : name,
            "job" : job
        }
        return requests.post(f"{self.BASE_URL}users", json=payload, headers=headers)

    def register_user(self, email: str, password: str):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        payload = {
            "email" : email,
            "password" : password
        }
        return requests.post(f"{self.BASE_URL}register", json=payload, headers=headers)

    def login(self, email: str, password: str):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        payload = {
            "email" : email,
            "password" : password
        }
        return requests.post(f"{self.BASE_URL}login", json=payload, headers=headers)