"""
Calculator module with interactive menu
"""
def calculator_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Choose operation: ")
    return choice

def calculate_with_menu(a, b, operation):
    if operation == '1':
        return a + b
    elif operation == '2':
        return a - b
    elif operation == '3':
        return a * b
    elif operation == '4':
        return a / b if b != 0 else None
    return None
