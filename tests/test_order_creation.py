import allure
from Api.api_client import ApiClient
from data import TestData, VALID_INGREDIENTS


@allure.feature("Создание заказа")
@allure.story("Тестирование функционала создания заказа с различными условиями")
class TestOrderCreate:

    @allure.title("Cоздания заказа с авторизацией")
    def test_create_order_authenticated(self, registered_user):
        with allure.step("Получаем токен авторизации из зарегистрированного пользователя"):
            access_token = registered_user["access_token"].replace("Bearer ", "")
            assert access_token, "Токен отсутствует"

        with allure.step("Создаем заказ с авторизацией"):
            api_client = ApiClient()
            ingredients = TestData.get_ingredients()
            response = api_client.create_order(access_token=access_token, ingredients=ingredients)

        with allure.step("Проверяем успешность создания заказа"):
            assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
            assert response.json().get("success") is True, "Не удалось создать заказ"

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthenticated(self):
        with allure.step("Создаем заказ без авторизации"):
            api_client = ApiClient()
            ingredients = TestData.get_ingredients()
            response = api_client.create_order(ingredients=ingredients)

        with allure.step("Проверяем успешность создания заказа без авторизации"):
            assert response.status_code == 200, f"Ожидаемый ответ 200, но вернулся {response.status_code}"
            assert response.json().get("success") is True, "Не удалось создать заказ"

    @allure.title("Cоздания заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        with allure.step("Создаем заказ с валидными ингредиентами"):
            api_client = ApiClient()
            ingredients = TestData.get_ingredients()
            response = api_client.create_order(ingredients=ingredients)

        with allure.step("Проверяем успешность создания заказа"):
            assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
            assert response.json().get("success") is True, "Не удалось создать заказ"

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_empty_ingredients(self):
        with allure.step("Создаем заказ без указания ингредиентов"):
            api_client = ApiClient()
            response = api_client.create_order()

        with allure.step("Проверяем ожидаемую ошибку"):
            assert response.status_code == 400, f"Ожидаемый ответ 400 Bad Request, но вернулся {response.status_code}"
            assert response.json().get("success") is False, "Ожидалась ошибка из-за отсутствия ингредиентов"

    @allure.title("Тест создания заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient(self):
        with allure.step("Создаем заказ с невалидным хешем ингредиента"):
            api_client = ApiClient()
            invalid_ingredients = ["invalid_hash_123"]
            response = api_client.create_order(ingredients=invalid_ingredients)

        with allure.step("Проверяем ожидаемую ошибку сервера"):
            assert response.status_code == 500, (
                f"Ожидаемый ответ 500 Internal Server Error, но вернулся {response.status_code}"
            )