"""
Language support for greetings
"""
GREETINGS = {
    'en': 'Hello',
    'es': 'Hola',
    'fr': 'Bonjour',
    'de': 'Hallo'
}

def greet_multilingual(name, lang='en'):
    """Greet in different languages"""
    greeting = GREETINGS.get(lang, GREETINGS['en'])
    return f"{greeting}, {name}!"

def get_supported_languages():
    """Return list of supported languages"""
    return list(GREETINGS.keys())
