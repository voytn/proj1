# app.py   основной файл приложения

def greet(name: str) -> str:
    """Возвращает приветственное сообщение."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
