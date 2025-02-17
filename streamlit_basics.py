import streamlit as st
import pandas as pd
import pandas  as pd
import numpy as np

# Title for the application
st.title("Hello world")
## Dispaly  a  SIMPLE  TEXT'
st.write("this is a simple text")
# Create   a datatframe
df=pd.DataFrame({
    "column 1":[1,2,3,4,5],
    "second column": [10,20,30,40,50]
})

#Display the dataframe
st.write("Hera is the Data Frame")
st.write(df)

# Create a  line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)