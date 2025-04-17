import json
import os

def load_language_map(language: str) -> dict:
    file_path = os.path.join("languages", f"{language}_map.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def translate_name(name: str, language_map: dict) -> str:
    name = name.lower()
    for key, value in language_map.items():
        name = name.replace(key, value)
    return name.capitalize()

def main():
    print("🌍 Welcome to Hermes: The Ancient Language Name Translator 🌍")
    name = input("Enter your name:\n> ")
    language = input("Choose a language [ex: latin]:\n > ").strip().lower() or "latin"

    try:
        lang_map = load_language_map(language)
    except FileNotFoundError:
        print(f"Error: Language {language} not yet supported.")
        return
    
    translated = translate_name(name, lang_map)
    print(f"\nIn {language.title()}, your name could be: {translated}")

if __name__ == "__main__":
    main()