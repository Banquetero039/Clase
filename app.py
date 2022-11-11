import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os, time

st.title('Los problemas de salud en Mexico')
st.image("https://www.limarp.com/img/obesidad-morbida.png")
st.sidebar.header("Filtro")
with st.sidebar:
  porcentaje = st.radio("Indice:",("Inicio","Graficas","Soluciones"))
  if porcentaje == "Baja california":
    st.write("80%")
  
  estatura = st.number_input("Ingresa tu estatura en metros",)
  st.write(estatura)
  
  masa = st.number_input("Ingresa tu masa en Kg")
  st.write(masa)
  
  imc = masa/estatura**2
  st.write(imc)

st.subheader("¿Cual es el problema de salud en Mexico?")
st.text_area("Las enfermedades no transmisibles siguen siendo uno de los principales retos que debemos afrontar en México, y es de la mano de la innovación y la investigación que podemos cambiar la ruta de estas enfermedades, y cambiar la vida de las personas, sus familias y sus comunidades.")

st.text("Gasto total en salud (publico y privado), por pais")
chart_data = pd.DataFrame(
    np.random.randn(17, 17),
    columns=["E.U", "Holanda", "Francia","Alemania","Canada","Belgica","U.K","OCDE","España","Brasil","Chile","Rep.Checa","Polonia","Cor.Sur","Mexico","Turquia","Rusia"])

st.bar_chart(chart_data)
