import streamlit as st

name = st.text_input("Имя разработчика", "Сальников Денис")
number = st.number_input(
    label="Вариант",
    min_value=1,
    max_value=10,
    value="min",
    step=1,

    )
st.title("Информация о разработчкике")
st.write("Имя: ", name)
st.write("Группа: ФИТ-231")
st.write("Вариант: ", number)
dataset = st.selectbox(
    label="Датасет",
    options=("Регрессия", "Классификация", "Кластеризация"),
    index=None,
    placeholder="Выберите датасет"
)

st.write("Выбранный датасет: ", dataset)
