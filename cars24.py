import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.title("Car prediction app")

col1, col2,col3, col4 =st.columns(4)
with col1:
    #use radio for fuel type
    fuel_type=st.radio('Fuel Type',['Petrol','Diesel','CNG','Electric'])
with col2:
    ## use transmission 
    Transmission_Type=st.selectbox('Transmission_Type',['Manual','Automatic'])
with col3:
    ## engine power
    engine_power=st.slider('Engine power',500,100,step=100)

with col4:
    ##Seats
    seats=st.selectbox("Select seats",[1,2,3,4,5,6,7])

# model=pickle.load(open('car_pred','rb'))
with open("car_pred", "rb") as f:
    model = pickle.load(f)

encode_dict={
    'Fuel Type':{'Petrol':2,'Diesel':1,'CNG':3, 'LPG':4,"Electric":5},
     'Transmission_Type':{'Manual':1, 'Automatic':2},

}

def model_pred(fuel_type,Transmission_Type,engine_power,seats):
    Transmission_Type=encode_dict["Transmission_Type"][Transmission_Type]
    fuel_type=encode_dict['Fuel Type'][fuel_type]

    data = [[2018.0, 1, 40000, fuel_type,Transmission_Type, 18.0, engine_power, 85, seats]]
    return round(model.predict(data)[0],2)

if st.button("Predict"):
    st.write(model_pred(fuel_type,Transmission_Type,engine_power,seats))
st.write("Click on predict once you're done with the data")



