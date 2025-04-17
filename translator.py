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

