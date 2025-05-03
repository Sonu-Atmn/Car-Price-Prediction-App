import streamlit as st
import pickle as pkl
import pandas as pd
import getimage



@st.cache_resource
def enco_and_params_load():
    #params
    with open(r'pickle_data\parametrs_details.pkl','rb') as file:
        data_params=pkl.load(file)
    #data encoding
    with open(r'pickle_data\car_encoder.pkl','rb') as file:
        encoder=pkl.load(file)
    return data_params,encoder


@st.cache_resource
def load_model():
    
    with open(r'pickle_data\car_model.pkl','rb') as file:
        car_model=pkl.load(file)
    return car_model

car_model=load_model()
data_params,encoder=enco_and_params_load()

def prediction(data):
    price_predicted=car_model.predict(pd.DataFrame(data))
    return price_predicted

def Taking_input():
    
    brand = st.selectbox("Brand",data_params['make'],placeholder="Choose a model")
    model= st.selectbox("Model",data_params['make_model'][brand])
    year=st.number_input("Model Year",min_value=2010,max_value=2025)
    km=st.number_input("Km Driven",0,500000,30000,step=5000)
    fuel=st.selectbox('Fuel Type',data_params['fuel'])
    owner=st.selectbox('Owner Detail',data_params['owner'])
    st.session_state.brand=brand
    st.session_state.model=model
    st.session_state.fuel=fuel
    st.session_state.owner=owner
    
    
    brand_encoded=encoder['maker'].transform([brand])
    model_encoded=encoder['model_name'].transform([model])
    fuel_encoded=encoder['fuel_type'].transform([fuel])
    owner_encoded=encoder['pre_owner'].transform([owner])
    
    return brand_encoded,model_encoded,year,km,fuel_encoded,owner_encoded 

def predict():
    
    st.header("Predict Your Car's Price")
    brand_e,model_e,year,km,fuel_e,owner_e=Taking_input()
    data={'model_year':[year],'maker':[brand_e],'model_name':[model_e],'km_driven':[km],'fuel_type':[fuel_e],'pre_owner':[owner_e]}
    
    check=False
    col1, col2, col3 = st.columns([2, 2, 1])
    with col2:
        if st.button('Predict Price'):
            check=True
            predicted_price=prediction(data)
            
    if check:
        st.markdown('<hr>',unsafe_allow_html=True)
        column1,column2=st.columns([1,1])
        with column1:
            st.markdown(f"""
                <style>
                    .brand-label {{
                        font-size: 28px;  /* Larger font for "Brand" */
                        font-weight: bold;
                        width: 150px;
                        margin-right: 10px;
                    }}
                    .brand-name {{
                        font-size: 25px;  /* Smaller font for "Suzuki" */
                        width: 200px;
                    }}
                </style>
                <span class="brand-label">Brand:</span><span class="brand-name">{st.session_state.brand}</span><br>
                <span class="brand-label">Model:</span><span class="brand-name">{st.session_state.model}</span><br>
                <span class="brand-label">Year:</span><span class="brand-name">{year}</span><br>
                <span class="brand-label">KM Driven:</span><span class="brand-name">{km}</span><br>
                <span class="brand-label">Fuel:</span><span class="brand-name">{st.session_state.fuel}</span><br>
                <span class="brand-label">Owner Details:</span><span class="brand-name">{st.session_state.owner}</span><br>
                """, unsafe_allow_html=True)
            
        with column2:
            keyword=st.session_state.brand+" "+st.session_state.model
            link=getimage.get_img_link(keyword)
            with st.spinner("Loading image..."):
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
                        <img class="zoom" src="{link}" width="400"/>
                    </div>
                    """,
                    unsafe_allow_html=True
                    )
        

        st.markdown(f"""
            <style>
                .price-container {{
                    font-family:'Papyrus';
                    font-size: 22px;
                    font-weight: 500;
                    color: #333;
                    text-align: center;
                    padding: 20px;
                }}
                .price-value {{
                    font-family: "Times New Roman";
                    font-size: 40px;
                    font-weight: bold;
                }}
            </style>

            <div class="price-container">
                Your predicted price is <span class="price-value"><br>₹ {round(predicted_price[0],-3)}</span>
            </div>
        """, unsafe_allow_html=True)

   
        