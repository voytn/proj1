"""
Utility functions for the application
"""

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

def calculate(a, b):
    """Simple calculation function"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def subtract(a, b):
    """Subtract b from a"""
    return a - b
ef divide(a, b):
    """Divide a by b"""
    if b == 0:
        return None
    return a / b

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
