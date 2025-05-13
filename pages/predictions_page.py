import streamlit as st
import pandas as pd
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.models_loader import ModelsLoader

st.markdown("# Предсказания")

models_loader = ModelsLoader()
models = {
    "Decision Tree": models_loader.load_dtc(),
    "Random Forest": models_loader.load_rfc(),
    "Gradient Boosting": models_loader.load_gbc(),
    "Stacking": models_loader.load_stacking(),
    "CatBoost": models_loader.load_cbc()
}

model = st.selectbox(
    label="Модель",
    options= models.keys(),
    index=None,
    placeholder="Выберите модель"
)

st.markdown("## Введите данные о рейсе для получения предсказания о задержке")

df = pd.read_csv(r"data/airlines_label_encoding.csv").dropna()

airline_codes = df["Airline"].unique()
airline = st.selectbox(
    label="Код авиакомпании",
    options=airline_codes,
    index=None,
    placeholder="Введите код авиакомпании"
)


flight = st.number_input(
    label="Номер рейса",
    min_value=1,
    value=None,
    step=1,
    placeholder="Введите номер рейса"
)


airport_from_codes = df["AirportFrom"].unique()
airport_from = st.selectbox(
    label="Код аэропорта вылета",
    options=airport_from_codes,
    index=None,
    placeholder="Введите код аэропорта вылета"
)


airport_to_codes = df["AirportTo"].unique()
airport_to = st.selectbox(
    label="Код аэропорта прибытия",
    options=airport_to_codes,
    index=None,
    placeholder="Введите код аэропорта прибытия"
)


days = {
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6,
    "Воскресенье": 7
}
day_of_week = st.selectbox(
    label="День недели",
    options=days.keys(),
    index=None,
    placeholder="Введите день недели полёта",
)
day = days.get(day_of_week)


time = st.number_input(
    label="Время вылета",
    min_value=0,
    max_value=1440,
    value=None,
    step=1,
    placeholder="Введите время вылета в минутах с начала суток"
)


length = st.number_input(
    label="Длительность полёта",
    min_value=0,
    value=None,
    step=1,
    placeholder="Введите длительность полёта в минутах"
)

if all(x is not None for x in [airline, flight, airport_from, airport_to, day, time, length]):
    X = np.array([airline, flight, airport_from, airport_to, day, time, length])
    predict = models[model].predict(X.reshape(1, -1))
    
    if predict == 0:
        st.markdown(":green[Задержки нет]")
    elif predict == 1:
        st.markdown(":red[Задержка есть]")
