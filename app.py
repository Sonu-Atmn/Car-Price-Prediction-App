import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Car Price Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import homepage
import prediction
import about
import model_performance
import data_insights




with st.sidebar:
    selected = option_menu(
        menu_title="Car Price App",
        options=["Home", "Predict Price", "Data Insights", "Model Performance", "About"],
        icons=["house", "car-front", "bar-chart", "activity", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )   


if selected == "Home":
    homepage.Homepage()

    
elif selected == "Predict Price":
    prediction.predict()
       
    
# Data Insights Page
elif selected == "Data Insights":
    data_insights.Insights()
    
#model performance        
elif selected == "Model Performance":
    model_performance.Performance()

    
# About Page
elif selected == "About":
    about.About()