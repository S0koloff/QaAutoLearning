import requests

class ReqresClient:
    BASE_URL = "https://reqres.in/api/"

    def get_users(self, page=1):
        return requests.get(f"{self.BASE_URL}users", params={"page" : page})

    def get_user(self, id=2):
        return requests.get(f"{self.BASE_URL}users/{id}")

    def create_user(self, name: str, job: str):
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        payload = {
            "name" : name,
            "job" : job
        }
        return requests.post(f"{self.BASE_URL}users", json=payload, headers=headers)