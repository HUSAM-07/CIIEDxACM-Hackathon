import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set the page title and icon
st.set_page_config(page_title="Awesome App", page_icon="🚀")

# Sidebar
st.sidebar.title("Navigation")
selected_category = st.sidebar.radio("Select a Category", ["Home", "Data Analysis", "Visualization", "About Us"])

# Home Page
if selected_category == "Home":
    st.title("Welcome to the Awesome App")
    st.write("Explore various categories and features in this app.")
    st.image("app_image.jpg", use_column_width=True)

# Data Analysis Page
if selected_category == "Data Analysis":
    st.title("Data Analysis")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        st.subheader("Data Preview")
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

# Visualization Page
if selected_category == "Visualization":
    st.title("Visualization")
    st.write("Explore interactive visualizations.")

    # Create sample data
    data = pd.DataFrame(np.random.rand(100, 2), columns=["X", "Y"])

    # Scatter Plot
    st.subheader("Scatter Plot")
    fig = px.scatter(data, x="X", y="Y")
    st.plotly_chart(fig)

    # Bar Chart
    st.subheader("Bar Chart")
    data_bar = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [30, 45, 22]})
    fig_bar = px.bar(data_bar, x="Category", y="Value")
    st.plotly_chart(fig_bar)

# About Us Page
if selected_category == "About Us":
    st.title("About Us")
    st.write("We are a team of developers creating amazing apps.")
    st.image("team_image.jpg", use_column_width=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Contact us at [email@example.com]")
st.sidebar.text("Made with ❤️ by the Awesome Team")
