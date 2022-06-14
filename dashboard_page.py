import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    return pd.read_csv("dashboard.csv")

df = load_data()

def show_dashboard_page():
    st.title("Jobs4U Salaries Dashboard")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels = data.index, autopct = "%1.1f%%", shadow = True, startangle = 90)
    ax1.axis("equal")

    st.write("""#### Number of entries per country""")
    st.pyplot(fig1)
    
    st.write("""#### Mean salary per country""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Mean salary per experience""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

