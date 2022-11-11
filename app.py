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
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=10)

st.pyplot(fig)
