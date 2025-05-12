import streamlit as st

NAME = "Сальников Денис"
GROUP = "ФИТ-231"
photo_path = "../data/photo.jpg"

contact_info_text = f"""
### Разработка Web-приложения для инференса моделей ML и анализа данных

Имя разработчика: {NAME}

Группа: {GROUP}
"""

col1, col2 = st.columns(2)

with col1:
    st.markdown(contact_info_text)

with col2:
    st.image(photo_path)