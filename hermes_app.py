import streamlit as st
import json
import os
from translator import load_language_map, translate_name, list_languages

st.set_page_config(page_title="Hermes", page_icon="🪐")

st.title("🪐 Hermes")
st.subheader("Transliterate your name to Latin, Greek, or Hebrew")

name = st.text_input("Enter your name", value="Theodore")

languages = list_languages()
language = st.selectbox("Choose a language", [lang.capitalize() for lang in languages])

if st.button("Translate"):
    lang_map = load_language_map(language.lower())
    translated = translate_name(name, lang_map)
    st.success(f"In {language.title()}, your name could be: **{translated}**")