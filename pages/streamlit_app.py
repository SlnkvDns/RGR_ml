import streamlit as st

pages = {
    "Страницы": [
        st.Page("contact_page.py", title="Информаци о разработчике"),
        st.Page("data_page.py", title="Датасет"),
        st.Page("predictions_page.py", title="Выбор модели")
    ]
}


pg = st.navigation(pages)
pg.run()
