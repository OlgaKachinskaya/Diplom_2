import pytest
import allure
from Api.api_client import ApiClient

class TestUserLogin:

    def test_login_success(self, registered_user):
        api_client = ApiClient()

        with allure.step("Готовим данные для входа"):
            login_data = {
                "email": registered_user["email"],
                "password": registered_user["password"]
            }

        with allure.step("Отправляем запрос на вход"):
            response = api_client.login_user(login_data["email"], login_data["password"])

        with allure.step("Проверяем успешный вход"):
            assert response.status_code == 200
            assert "accessToken" in response.json()
            assert response.json()["user"]["email"] == registered_user["email"]

    def test_login_with_wrong_credentials(self, registered_user):
        api_client = ApiClient()

        with allure.step("Готовим неверные данные для входа"):
            wrong_login_data = {
                "email": registered_user["email"],
                "password": "wrong_password"
            }

        with allure.step("Отправляем запрос с неверными данными"):
            response = api_client.login_user(wrong_login_data["email"], wrong_login_data["password"])

        with allure.step("Проверяем ошибки авторизации"):
            assert response.status_code == 401
            assert response.json()["message"] == "email or password are incorrect"