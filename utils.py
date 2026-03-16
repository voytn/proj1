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
def greet_formal(name):
    """Formal greeting"""
    return f"Good day, {name}."

def greet_informal(name):
    """Informal greeting"""
    return f"Hey {name}!"

def greet_time_based(name):
    """Time-based greeting"""
    from datetime import datetime
    hour = datetime.now().hour
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"
