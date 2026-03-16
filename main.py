#!/usr/bin/env python3
"""
Main entry point for the application
"""
import sys
from utils import greet, calculate, multiply, subtract, divide
from config import DEBUG, VERSION
from calculator import calculate_with_menu, calculator_menu

def main():
    print(f"Starting application v{VERSION}")
    print(f"Debug mode: {DEBUG}")
    
    name = "World" if len(sys.argv) < 2 else sys.argv[1]
    print(greet(name))
    
    # Calculator demo
    print("\n=== Calculator Demo ===")
    choice = calculator_menu()
    result = calculate_with_menu(10, 5, choice)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
