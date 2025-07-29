import pytest
import allure
from data import TestData
from Api.api_client import ApiClient

class TestUserCreation:

    def test_create_user_success(self):
        api_client = ApiClient()

        with allure.step("гененрируем данные нового пользователя"):
            user_data = TestData.create_user()

        with allure.step("Отправляем запроа на регистрацию через api_client"):
            response = api_client.register_user(user_data)

        with allure.step("Проверяем ответ"):
            assert response.status_code == 200, "Ожидается статус код 200"
            assert "accessToken" in response.json(), "В ответе должен быть accessToken"
            assert response.json()["user"]["email"] == user_data["email"], "Email должен совпадать с отправленным"

    def test_create_existing_user(self, registered_user):
        api_client = ApiClient()

        with allure.step("Готовим данные уже зарегистрированного пользователя"):
            existing_user = {
                "email": registered_user["email"],
                "password": registered_user["password"],
                "name": registered_user["name"]
            }

        with allure.step("Повторная отправка запроса на регистрацию"):
            response = api_client.register_user(existing_user)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 403, "Ожидается статус код 403 для существующего пользователя"
            assert response.json()["message"] == "User already exists", "Сообщение об ошибке должно соответствовать"

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        api_client = ApiClient()

        with allure.step(f"Генерация пользователя с пропущенным полем '{missing_field}'"):
            user_data = TestData.create_user()
            user_data.pop(missing_field)

        with allure.step("Отправка запроса с неполными данными"):
            response = api_client.register_user(user_data)

        with allure.step("Проверка валидации"):
            assert response.status_code == 403, "Ожидается статус код 403 при отсутствии обязательного поля"
            assert response.json()["message"] == "Email, password and name are required fields", "Сообщение об ошибке должно соответствовать"