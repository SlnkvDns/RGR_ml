import streamlit as st

pages = {
    "Страницы": [
        st.Page("contact_page.py", title="Информаци о разработчике", icon="💁‍♂️"),
        st.Page("data_page.py", title="Датасет", icon="🔢"),
        st.Page("visualization_page.py", title="Визуализации", icon="📊"),
        st.Page("predictions_page.py", title="Предсказание", icon="🔮")
    ]
}


pg = st.navigation(pages)
pg.run()
