import streamlit as st

NAME = "Сальников Денис"
GROUP = "ФИТ-231"
VARIANT = "1"

st.title("Информация о разработчкике")
st.text_input("Имя разработчика: ", NAME)
st.text_input("Группа: ", GROUP)
st.text_input("Вариант датасета: ", VARIANT)
