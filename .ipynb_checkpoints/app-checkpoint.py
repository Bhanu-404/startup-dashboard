import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#Data
file = pd.read_csv('Data Filtered.csv')
file['date'] = pd.to_datetime(file['date'], errors = 'coerce')
file['year'] = file['date'].dt.year
print(file.info())
company_names = np.sort(file['startup'].unique())
#SideBar

st.sidebar.title("Startup Funding")
option = st.sidebar.selectbox('Select an option', ['Overall analysis', 'Individual Analysis', 'Investor'])

#Investor analysis
def load_investor(investor):
    """Loads the data of the investor"""
    data = file[file['investor'].str.contains(investor)][['date', 'startup', 'Industry Vertical', 'city', 'amount']].head()
    st.dataframe(data)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Total Investments by {investor}")
        big_investments = file[file['investor'].str.contains(investor)].groupby('startup')['amount'].sum().head()
        fig, ax = plt.subplots()
        ax.bar(big_investments.index, big_investments.values, color='skyblue')
        ax.set_xlabel("Startup")
        ax.set_ylabel("Investment Amount")
        ax.set_title(f"Total Investments by {investor}")
        ax.tick_params(axis='x', labelsize=7, rotation=30)
        ax.tick_params(axis='y', labelsize=7)
        st.pyplot(fig)


    col3, col4, col5 = st.columns(3)

    with col3:
        sector_investments = file[file['investor'].str.contains(investor, na=False)] \
                            .groupby('Industry Vertical')['amount'].sum()
        st.subheader(f"Investments in each sector by {investor}")
        fig, ax = plt.subplots(figsize=(4, 4))  
        ax.pie(sector_investments, labels=sector_investments.index, autopct='%1.1f%%', 
            colors=plt.cm.Paired.colors, startangle=90, wedgeprops={'edgecolor': 'black'})
        ax.set_title(f"Total Investments by {investor}")
        st.pyplot(fig)

    with col4:
        sector_investments = file[file['investor'].str.contains(investor, na=False)] \
                            .groupby('city')['amount'].sum()
        st.subheader(f"Investments in each city by {investor}")
        fig, ax = plt.subplots(figsize=(4, 4))  
        ax.pie(sector_investments, labels=sector_investments.index, autopct='%1.1f%%', 
            colors=plt.cm.Paired.colors, startangle=90, wedgeprops={'edgecolor': 'black'})
        ax.set_title(f"Total Investments by {investor}")
        st.pyplot(fig)

    with col5:
        sector_investments = file[file['investor'].str.contains(investor, na=False)] \
                            .groupby('round')['amount'].sum()
        st.subheader(f"Investments in each round by {investor}")
        fig, ax = plt.subplots(figsize=(4, 4))  
        ax.pie(sector_investments, labels=sector_investments.index, autopct='%1.1f%%', 
            colors=plt.cm.Paired.colors, startangle=90, wedgeprops={'edgecolor': 'black'})
        ax.set_title(f"Total Investments by {investor}")
        st.pyplot(fig)

    col6, col7 = st.columns(2)
    with col6:
        st.subheader(f"Year to year investments of {investor}")
        yoy = file[file['investor'].str.contains(investor)].groupby('year')['amount'].sum()
        fig, ax = plt.subplots()
        ax.set_xlabel("Year")
        ax.set_ylabel("Investment Amount")
        ax.plot(yoy.index, yoy.values, marker='o', color='b')
        st.pyplot(fig)

    #similar investors
    investor1 = file[file['investor'].str.contains(investor)]['Industry Vertical']
    investor2 = file[file['investor'].str.contains('Sequoia India')]['Industry Vertical']

    arr = np.intersect1d(investor1, investor2)

    st.subheader(f"Similar investment sectors between {investor} and Sequoia India")
    similar_df = pd.DataFrame(arr, columns=['Sector'])
    st.dataframe(similar_df)


if option == "Overall analysis":
    st.title("Overall Analysis")
elif option == "Individual Analysis":
    st.title("Company Analysis")
    st.sidebar.selectbox("Select a company", company_names)
    btn1 = st.sidebar.button("Start Analysis")
elif option == "Investor":
    investor = st.sidebar.selectbox("Select an investor", sorted(set(file.investor.str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor")
    if btn2:
        load_investor(investor)