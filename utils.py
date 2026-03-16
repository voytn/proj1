# utils.py   вспомогательные функции

def to_uppercase(text: str) -> str:
    return text.upper()

def to_lowercase(text: str) -> str:
    return text.lower()
Сохраните. Затем:
nano config.py
Введите:
# config.py   настройки приложения

APP_NAME = "MyApp"
DEBUG = False
MAX_RETRIES = 3
# Used by: app.py

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return None
    return a / b
