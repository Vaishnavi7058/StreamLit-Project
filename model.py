import streamlit as st
import pickle

st.set_page_config(page_title="Wine Price Prediction", page_icon=":wine_glass:", layout="wide")

st.title(":heavy_dollar_sign: Wine Price Prediction :wine_glass:")

model1 = pickle.load(open('gbr1.pkl', 'rb'))
model2 = pickle.load(open('adr1.pkl', 'rb'))

c1, c2 = st.columns(2)

n1 = c1.number_input("Fixed Acidity")
n2 = c2.number_input("Volatile Acidity")
n3 = c1.number_input("Citric Acid")
n4 = c2.number_input("Residual Sugar")
n5 = c1.number_input("Chlorides")
n6 = c2.number_input("Free Sulfur Dioxide")
n7 = c1.number_input("Total Sulfur Dioxide")
n8 = c2.number_input("Density")
n9 = c1.number_input("pH")
n10 = c2.number_input("Sulphates")
n11 = c1.number_input("Alcohol")
n12 = c2.number_input("Quality")

new_feature = [[n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]]

c3, c4 = st.columns(2)

if c3.button("GBR Model prediction"):
    t1 = model1.predict(new_feature)
    c3.subheader(t1)

if c4.button("ADR Model prediction"):
    t2 = model2.predict(new_feature)
    c4.subheader(t2)
