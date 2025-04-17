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

def list_languages():
    files = os.listdir("languages")
    return [file.replace("_map.json", "") for file in files if file.endswith("_map.json")]

def main():
    print("🌍 Welcome to Hermes: The Ancient Language Name Translator 🌍")
    name = input("Enter your name:\n> ")

    languages = list_languages()
    print(f"\nAvailable Languages: {', '.join([lang.upper() for lang in languages])}")
    language = input("Choose a language [ex: latin]:\n > ").strip().lower() 

    while language not in languages:
        print(f"Error: Language {language} not yet supported.")
        language = input("Choose a language [ex: latin]:\n > ").strip().lower() 
    
    lang_map = load_language_map(language)
    translated = translate_name(name, lang_map)

    print(f"In {language.title()}, your name could be: {translated}")


if __name__ == "__main__":
    main()