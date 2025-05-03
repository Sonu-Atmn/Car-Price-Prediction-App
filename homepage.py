import streamlit as st
import base64


with open("porche.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

def Homepage():
    st.markdown("<h1 style='text-align: center;'>Used Car price Prediction</h1>", unsafe_allow_html=True)

    st.markdown(
    f"""
    <style>
    .zoom {{
        transition: transform 0.3s;
        display: block;
        margin: auto;
        padding: 20px;
    }}
    .zoom:hover {{
        transform: scale(1.07);
    }}
    </style>

    <div class="image-container">
        <img class="zoom" src="data:image/png;base64,{encoded_image}" width="400"/>
    </div>
    """,
    unsafe_allow_html=True
    )
    
   
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        .welcome-text {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-size: 20px;
            color: #2c3e50;
            padding: 20px 10px;
        }
    </style>
    <div class="welcome-text">
        Welcome to the Car Price Predicton App. Input your car's details to get an instant price prediction. 
        Explore data trends and model performance in other sections.
    </div>
    """, unsafe_allow_html=True)
