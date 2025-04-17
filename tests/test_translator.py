import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import translator

def test_translate_name_basic():
    test_map = {
        "ph": "f",
        "ae": "æ",
        "j": "i"
    }
    result = translator.translate_name("Jaeph", test_map)
    assert result == "Iæf"