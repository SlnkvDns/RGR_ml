import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

@st.cache_data
def visualize():
    FIG_SIZE = (10, 8)

    df = pd.read_csv(r"data/airlines_label_encoding.csv", index_col=0)

    fig1, axs1 = plt.subplots(figsize=FIG_SIZE)
    days_delay = df.groupby(by='DayOfWeek')['Delay'].sum().sort_index(ascending=False)
    labels = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    axs1.pie(days_delay, labels=labels, autopct='%1.1f%%')

    n = 100
    intervals = np.linspace(df['Length'].min(), df['Length'].max(), n+1)
    percent_delay = []
    for i in range(len(intervals) - 1):
        percent_delay.append(df.query(f'Length >= {intervals[i]} & Length < {intervals[i+1]}')['Delay'].sum() / df.shape[0]*100)
        
    fig2, axs2 = plt.subplots(figsize=FIG_SIZE)
    axs2.bar(intervals[:-1], height=percent_delay, width=df['Length'].max()/n)


    fig3, axs3 = plt.subplots(figsize=FIG_SIZE)
    df.boxplot(by='DayOfWeek', column=['Length'], ax=axs3)

    fig4, axs4 = plt.subplots(figsize=FIG_SIZE)
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', ax=axs4)


    st.markdown("# Визуализация зависимостей")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Распределение задержек по дням недели")
        st.pyplot(fig1)
        
        st.markdown("### Зависимость длительности полёта от дня недели")
        st.pyplot(fig3,)

    with col2:
        st.markdown("### Корреляционная матрица")
        st.pyplot(fig4)
        
        st.markdown("### Вероятность задержки от длительности полёта")
        st.pyplot(fig2)


visualize()
