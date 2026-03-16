#!/usr/bin/env python3
"""
Main entry point for the application
"""
import sys
from utils import greet, calculate, multiply, greet_formal, greet_informal, greet_time_based
from config import DEBUG, VERSION
from languages import greet_multilingual, get_supported_languages

def main():
    print(f"Starting application v{VERSION}")
    print(f"Debug mode: {DEBUG}")
    
    name = "World" if len(sys.argv) < 2 else sys.argv[1]
    
    # Greeting demo
    print(f"\nStandard: {greet(name)}")
    print(f"Formal: {greet_formal(name)}")
    print(f"Informal: {greet_informal(name)}")
    print(f"Time-based: {greet_time_based(name)}")
    
    # Multilingual demo
    print(f"\nSpanish: {greet_multilingual(name, 'es')}")
    print(f"French: {greet_multilingual(name, 'fr')}")
    
    result = calculate(10, 5)
    print(f"\nCalculation result: {result}")

if __name__ == "__main__":
    main()





    result = calculate(10, 5)
    print(f"\nCalculation result: {result}")

if __name__ == "__main__":
    main()
