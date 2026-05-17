import streamlit as st
from database.db import conn

st.set_page_config(
    page_title="Expense Splitter",
    layout="centered"
)

st.title('Expense Splitter')
st.write('Welcome to Expense Splitter')
st.success('Database connected')


name = st.text_input('Enter user name')

if st.button('Add user'):
    conn.execute("INSERT INTO users (name) VALUES (?)",(name,))

    conn.commit()

    st.success('User added')

#Display users
users = conn.execute("SELECT * FROM users").fetchall()

st.subheader('Users')

for user in users:
    st.write(user[1])

    