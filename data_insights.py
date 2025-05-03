import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # text=st.text('Loading Data...')
    path=r"Pre-Owned Car Resale in India-2021.csv"
    data=pd.read_csv(path)
    return data

def Insights():
    st.header("Data Insights")
    st.write('In the automotive industry, determining the price of a car involves various factors, such as brand reputation, car features, horsepower, and fuel efficiency. Car price prediction is a crucial application of machine learning. This project is designed to help you learn how to build a model for car price prediction.')
    data=load_data()
    
    top10carmaker=data.groupby(by='maker')['price (₹)'].mean()
    sorted_top10brand = top10carmaker.sort_values(ascending=False)[:10]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=sorted_top10brand.index,
        y=sorted_top10brand.values,
        mode='lines+markers',
        name='Top 10 Car Makers',
        marker_color='#4B2E2E'
    ))

    fig.update_layout(
        title='Top 10 Car Makers',
        xaxis_title='Car Maker',
        yaxis_title='Average Price ₹'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    fig = px.scatter(
    data,
    x='distance_covered (km)',
    y='price (₹)',
    title='Price vs Distance Covered',
    labels={'distance_covered (km)': 'Kilometers Driven', 'price (₹)': 'Asking Price'},
    opacity=0.6,
    trendline='ols'
    )
    st.plotly_chart(fig, use_container_width=True)

    


    
    year_avg_price=data.groupby(by='model_year')['price (₹)'].mean()

    fig = go.Figure()


    fig.add_trace(go.Bar(
        x=year_avg_price.index,  # The 'index' is the Year
        y=year_avg_price.values,  # The 'values' is the Average Price
        text=year_avg_price.values,  # Text on bars for price
        texttemplate='%{text:.2s}',  # Format price to two significant digits
        textposition='outside',
        marker_color='#4B2E2E'
    ))


    fig.update_layout(
        title='Average Price by Year',
        xaxis_title='Year',
        yaxis_title='Average Price (₹)',
        title_font_size=20,
        title_x=0.5,  # Center the title
    )


    st.plotly_chart(fig, use_container_width=True)

