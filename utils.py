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
