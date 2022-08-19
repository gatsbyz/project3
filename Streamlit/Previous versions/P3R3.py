from click import option
import streamlit as st



import pandas as pd
from pathlib import Path

st.write("# EtherCAR RENTAL CAR!")
st.write("By BlueSky")

titleIMG = ("Title.PNG")
st.image(titleIMG)

st.write("# Hi, this is Blue Skys first web app! :sunglasses:")

#Price Chart import
Price1Chart = pd.read_csv(
    Path("PriceChart1.csv"),
    infer_datetime_format=False)
df = pd.DataFrame(Price1Chart)


st.write(df)

#Image Data
Mid_Size = ("mid.jpg")
lux = ("lux.jpg")
MiniVan = ("Mini.jpg")
Comp = ("COMP.jpg")


#Car selection
st.write("# Pick your Car!")

if st.button("Mid-Sized!"):
     st.image(Mid_Size)

if st.button("Compact Car!"):
    st.image(Comp)

if st.button("Luxary Car!"):
    st.image(lux)

if st.button("MiniVan"):
    st.image(MiniVan)