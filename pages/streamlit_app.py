import streamlit as st

pages = {
    "Страницы": [
        st.Page("contact_page.py", title="Информаци о разработчике"),
        st.Page("data_page.py", title="Датасет")
    ]
}


pg = st.navigation(pages)
pg.run()
