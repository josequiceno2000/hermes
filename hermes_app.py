import streamlit as st
import json
import os
from translator import load_language_map, translate_name, list_languages

st.set_page_config(page_title="Hermes: Ancient Name Translator", page_icon="🪐")

st.title("🪐 Hermes: Ancient Language Name Translator")
st.subheader("Discover how your name would sound in Latin, Greek, and Hebrew!")

name = st.text_input("Enter your name", value="Theodore")

languages = list_languages()
language = st.selectbox("Choose a language", languages)

if st.button("Translate"):
    lang_map = load_language_map(language)
    translated = translate_name(name, lang_map)
    st.success(f"In {language.title()}, your name could be: **{translated}**")