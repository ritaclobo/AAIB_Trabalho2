import streamlit as st
import pandas as pd

st.write("Cloud Logger de Instrumentação")

st.write("Gráfico")

chart_data = pd.DataFrame(
  np.random.randn(10,2)
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)
