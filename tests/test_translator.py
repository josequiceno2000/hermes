import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import translator

def test_translate_name_latin():
    latin_map = {
        "ph": "f",
        "ae": "æ",
        "j": "i"
    }
    assert translator.translate_name("Jaeph", latin_map) == "Iæf"

def test_translate_name_greek():
    greek_map = {
        "ph": "φ",
        "th": "θ",
        "ch": "χ",
        "ps": "ψ",
        "x": "ξ",
        "r": "ρ",
        "y": "υ",
        "i": "ι",
        "l": "λ",
        "s": "ς",
        "u": "υ",
        "o": "ο"
    }
    assert translator.translate_name("Thorphiulos", greek_map) == "Θορφιυλος"