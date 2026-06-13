class Urls:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    CHANGE_USER = f"{BASE_URL}/api/auth/user"
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    GET_USER_ORDERS = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"


class ErrorMessages:
    USER_EXISTS = "User already exists"
    MISSING_FIELDS = "Email, password and name are required fields"
    LOGIN_INCORRECT = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"
    NO_INGREDIENTS = "Ingredient ids must be provided"


class TestData:
    VALID_INGREDIENTS = ["60d3463f7034a000269f45e7", "60d3463f7034a000269f45e9"]
    INVALID_HASH = "invalid_hash_123"