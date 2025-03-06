import streamlit as st
import pandas as pd
import time

#text based utility

st.title("Startup Dashboard")
st.header("I love streamlit!")
st.subheader("And I am loving it!!")
st.write("this is just like a paragraph tag")

st.markdown("""
# This is a header 
## This is a header 
### This is a header 
""")

st.code("""
def square(a):
    return a**2

x = square(5)
print(x)
""")

st.latex("x^2 + y^2 + 2xy = 0")

#displaying elements

df = pd.DataFrame({
    'name': ['Bhanu', 'Srinu', 'Laxman'],
    'marks': [100, 90, 80],
    'package': [14, 12, 10]
})

st.dataframe(df)

st.metric("Revenue in dollars", "15000$", "3%")

#json

st.json({
    'name': ['Bhanu', 'Srinu', 'Laxman'],
    'marks': [100, 90, 80],
    'package': [14, 12, 10]
})

#using media

st.image("download.jpeg")
# st.audio("")
# st.video("")

#sidebar and columns

st.sidebar.title("Sidebar Title")

col1, col2 = st.columns(2)

with col1:
    st.image("download.jpeg")
with col2:
    st.image("download.jpeg")

#STATUS
# error and success

st.error("Login Failed")
st.success("Login success")
st.info("no need to reload")
st.warning("Don't touch")

#progress bar

progress = st.progress(0)

for i in range(100):
    # time.sleep(0.1)
    progress.progress(i)

# TAKING USER INPUTS

email = st.text_input("Enter email: ")
password = st.text_input("Enter password: ")
number = st.number_input("Enter password: ")