import requests
from data import ENDPOINTS  # Импорт только ENDPOINTS (TestData не нужен)


class ApiClient:

    def register_user(self, user_data):
        return requests.post(ENDPOINTS["register"], json=user_data)

    def login_user(self, email, password):
        login_data = {"email": email, "password": password}
        return requests.post(ENDPOINTS["login"], json=login_data)

    def create_order(self, access_token=None, ingredients=None):
        headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}
        payload = {"ingredients": ingredients or []}
        return requests.post(ENDPOINTS["orders"], headers=headers, json=payload)