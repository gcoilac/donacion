from django.core.validators import MaxValueValidator, MinValueValidator

NULLABLE = {"null": True, "blank": True}
NOTNULLABLE = {"null": False, "blank": False}
DEFAULT_CHAR = {"max_length": 255}
TINI_TEXT = {"max_length": 1024}
DEFAULT_DECIMAL = {"max_digits": 24, "decimal_places": 4}
EXTENDED_DECIMAL = {"max_digits": 24, "decimal_places": 9}
DECIMAL_PERCENTAGE = {
    "max_digits": 5,
    "decimal_places": 2,
    "validators": [MinValueValidator(0.00), MaxValueValidator(100.00)],
}