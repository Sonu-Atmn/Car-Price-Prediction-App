import streamlit as st
import pickle as pkl
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


def Performance():
    st.header('Model used')
    st.markdown('<h5>RandomForestRegressor</h5>', unsafe_allow_html=True)
    st.header("Model Performance")
    with open(r'pickle_data\Y_test_y_pred.pkl','rb') as file:
        y=pkl.load(file)
        
    y_pred = y['y_pred']
    y_test=y['y_test']
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
        st.metric("R² Score", f"{r2_score(y_test, y_pred):.2f}")


    fig5 = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual Price', 'y': 'Predicted Price'},
                      title="Actual vs Predicted Prices")
    st.plotly_chart(fig5)
    
    
