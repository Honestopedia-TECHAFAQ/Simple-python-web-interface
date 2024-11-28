import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data(option):
    if option == "Sales Data":
        dates = pd.date_range(start="2024-01-01", periods=10)
        values = np.random.randint(100, 500, size=10)
        return pd.DataFrame({"Date": dates, "Sales": values})
    elif option == "User Growth":
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        values = np.cumsum(np.random.randint(50, 150, size=10))
        return pd.DataFrame({"Month": months, "Users": values})
    elif option == "Revenue":
        quarters = ["Q1", "Q2", "Q3", "Q4"]
        values = [np.random.randint(1000, 5000) for _ in quarters]
        return pd.DataFrame({"Quarter": quarters, "Revenue": values})

st.title("Interactive Data Viewer")

text_input1 = st.text_input("Enter first input:")
text_input2 = st.text_input("Enter second input:")

dropdown_options = ["Sales Data", "User Growth", "Revenue"]
selected_option = st.selectbox("Select a dataset to view:", dropdown_options)

if selected_option:
    st.subheader(f"Displaying data for: {selected_option}")
    data = get_data(selected_option)

    if selected_option == "Sales Data":
        fig, ax = plt.subplots()
        ax.plot(data["Date"], data["Sales"], marker='o', color="blue")
        ax.set_title("Sales Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        st.pyplot(fig)
    elif selected_option == "User Growth":
        fig, ax = plt.subplots()
        ax.bar(data["Month"], data["Users"], color="green")
        ax.set_title("User Growth by Month")
        ax.set_xlabel("Month")
        ax.set_ylabel("Users")
        st.pyplot(fig)
    elif selected_option == "Revenue":
        fig, ax = plt.subplots()
        ax.bar(data["Quarter"], data["Revenue"], color="orange")
        ax.set_title("Revenue by Quarter")
        ax.set_xlabel("Quarter")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)

if text_input1 or text_input2:
    st.write("Your inputs:")
    st.write(f"Input 1: {text_input1}")
    st.write(f"Input 2: {text_input2}")
