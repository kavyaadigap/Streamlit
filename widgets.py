import streamlit as st
import pandas as pd
st.title("streamlit text input")
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}")
age=st.slider("Select your age:",0,100,24)
st.write(f"you are {age} years old!  oh my god!!")
options=["Python", "Java","C++","Javascript"]
choice=st.selectbox("Chose your favarite Language:",options)
st.write(f"you selected {choice}.")
data={
    "Name":["Kavya","Ramya","Navya"],
    "Age":[24,25,240],
    "City":["Mlore","blore","Mlore"]
}
df=pd.DataFrame(data)
st.write(df)
uploaded_file=st.file_uploader("chose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)