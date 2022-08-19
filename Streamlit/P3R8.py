from calendar import Calendar
from click import option
import streamlit as st



import pandas as pd
from pathlib import Path
st.write("# Hi, this is BlueSkys first web app!:sunglasses:")
st.write("")
st.write("# EtherCAR RENTAL CAR!")
st.write("By BlueSky")

titleIMG = ("Streamlit_Resources/Title.PNG")
st.image(titleIMG)



#Price Chart import
Price1Chart = pd.read_csv(
    Path("Streamlit_Resources/PriceChart1.csv"),
    infer_datetime_format=False)
PriceChartDF = pd.DataFrame(Price1Chart)

st.write(PriceChartDF)


#Image Data
Mid_Size = ("Streamlit_Resources/mid.jpg")
lux = ("Streamlit_Resources/lux.jpg")
MiniVan = ("Streamlit_Resources/Mini.jpg")
Comp = ("Streamlit_Resources/COMP.jpg")
SUV = ("Streamlit_Resources/SUV.jpg")
Exotic = ("Streamlit_Resources/Exotic.jpg")

#Car selection
st.write("# Pick your Car!")

if st.button("Mid-Sized!"):
     st.image(Mid_Size)

if st.button("Compact Car!"):
    st.image(Comp)

if st.button("Luxary Car!"):
    st.image(lux)

if st.button("MiniVan!"):
    st.image(MiniVan)

if st.button("SUV!"):
    st.image(SUV)

if st.button("Exotic!"):
    st.image(Exotic)






#Sidebar selection

#Hours or days sidebar selection
H_R = ["Hours", "Days"]
hours_days = st.sidebar.selectbox("Hours or Days?", H_R)


#Number of Hours or Days sidebar selection
number_of_H_R = st.sidebar.number_input("Number of Hours/Days?")

#Day of Rental selection
calendar_input = st.sidebar.date_input("Please select your rental date: ",value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Time of Rental Selection
time_input = st.sidebar.time_input("Please select your ", value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Rental book button!
if st.sidebar.button("Book your EtherCar!!"):
    st.sidebar.write("Succsess!")
    st.sidebar.write("Thank your for using EtherCar!!")
    st.sidebar.write("Enjoy your trip!")