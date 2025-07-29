import random
import string

def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_user():
    random_part = generate_random_string(6)
    return {
        "email": f"{random_part}@example.com",
        "password": generate_random_string(10),
        "name": f"User-{random_part}"
    }

def generate_ingredients(available_ingredients, count=2):
        return random.sample(available_ingredients, min(count, len(available_ingredients)))

