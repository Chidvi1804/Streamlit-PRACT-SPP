import pandas as pd
import numpy as np
import streamlit as st

st.title("Streamlit Visualizations")

st.subheader("Line Chart")
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.line_chart(chart_data)

st.subheader("Bar Chart")
bar_data=pd.DataFrame(
    {"Fruits":["a","b","c"],
     "Amount":[10,1,12]}
)

st.bar_chart(bar_data.set_index("Fruits"))