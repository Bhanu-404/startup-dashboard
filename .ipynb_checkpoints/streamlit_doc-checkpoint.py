import streamlit as st
import pandas as pd

email = st.text_input("Enter email: ")
password = st.text_input("Enter password: ", type = 'password')

#adding dropdown
gender = st.selectbox('Select gender', ['Male', 'Female', 'others'])

btn = st.button("Register")

if btn:
        st.success("Registered successfully")
        st.balloons()
        st.write(gender)
        st.write(email)
        # registered.append(email)
        st.write(password)
        st.write(btn)

s = "sa"

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
    s = 0

st.write(s)
