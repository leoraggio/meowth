import streamlit as st


st.title("Register a New Transaction")


categories = ["Alimentação", "Moradia"]

with st.form("register"):
    col1, col2, col3 = st.columns(3)
    date = col1.date_input("date")
    amount = col2.number_input("amount")
    category = col3.selectbox("category", categories)

    description = st.text_area("description")

    submitted = st.form_submit_button()

    if submitted:
        st.write("date:", date)
        st.write("amount:", amount)
        st.write("category:", category)
