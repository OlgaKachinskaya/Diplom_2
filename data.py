from generators import generate_user, generate_ingredients


BASE_URL = "https://stellarburgers.nomoreparties.site/api"


ENDPOINTS = {
    "register": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "orders": f"{BASE_URL}/orders",
    "ingredients": f"{BASE_URL}/ingredients",
    "user": f"{BASE_URL}/auth/user",
}

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d", # Флюоресцентная булка
    "61c0c5a71d1f82001bdaaa76", #хрустящие минеральные кольца
    "61c0c5a71d1f82001bdaaa6e", #филе Люминесцентного тетраодонтимформа
    "61c0c5a71d1f82001bdaaa7a" #сыр с астероидной плесенью
]


class TestData:
    @staticmethod
    def create_user():
        return generate_user()

    @staticmethod
    def get_ingredients():
        return generate_ingredients(VALID_INGREDIENTS)