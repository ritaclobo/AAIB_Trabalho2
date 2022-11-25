import streamlit as st
import pandas as pd

self.construct_sidebar(5)

st.title("Cloud Logger de Instrumentação")

st.write("Gráfico")

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)

