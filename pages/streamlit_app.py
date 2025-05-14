import streamlit as st

pages = {
    "Страницы": [
        st.Page("contact_page.py", title="Информаци о разработчике"),
        st.Page("data_page.py", title="Датасет"),
        st.Page("visualization_page.py", title="Визуализации"),
        st.Page("predictions_page.py", title="Предсказание")
    ]
}


pg = st.navigation(pages)
pg.run()
