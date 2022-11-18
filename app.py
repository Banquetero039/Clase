import streamlit as st
import pandas as pd
import numpy as np
import os, time

opciones = st.sidebar.radio("Filtro",["Inicio","Graficas","Soluciones"])

if opciones =="Inicio":
  st.title('Los problemas de salud en Mexico')
  st.image("https://www.limarp.com/img/obesidad-morbida.png")
  st.subheader("¿Cual es el problema de salud en Mexico?")
  col1, col2 = st.columns(2)
  with col1:
    st.write("Las enfermedades no transmisibles siguen siendo uno de los principales retos que debemos afrontar en México, y es de la mano de la innovación y la investigación que podemos cambiar la ruta de estas enfermedades, y cambiar la vida de las personas, sus familias y sus comunidades.")
  with col2:
    st.image("https://cdn-3.expansion.mx/36/cb/5d3bf5384070b9e59b42ad28d8f9/mexico-gordo-1.jpg")
  st.subheader("¿Por que Mexico ocupa el primer lugar en obesidad infantil?")
  col3, col4 = st.columns(2)
  with col3:
    st.image("https://draalejandraramirez.com.mx/wp-content/uploads/2022/07/obesidad-infantil-scaled.jpg")
  with col4:
      st.write("El principal problema de nutrición que padecen niñas y niños de entre 6 a 11 años es la presencia de ambos padecimientos, obesidad y sobrepeso.Debido a esto, México se encuentra entre los primeros lugares en obesidad infantil en el mundo.El sobrepeso y la obesidad en México son un problema que se presenta desde la primera infancia, es decir, entre 0 y 5 años. Al menos 1 de cada 20 niños y niñas menores de 5 años padece obesidad, lo que favorece el sobrepeso durante el resto de su vida y los pone en riesgo de sufrir enfermedades circulatorias, del corazón y de los riñones, diabetes, entre otras.")
  st.subheader("‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ Diabetes‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ")
  st.write("La diabetes es una enfermedad crónica (de larga duración) que afecta la forma en que el cuerpo convierte los alimentos en energía.")
  st.write("Su cuerpo descompone la mayor parte de los alimentos que come en azúcar (también llamada glucosa) y los libera en el torrente sanguíneo.")
if opciones =="Graficas":
  st.title("Recursos destinados a la salud")
  st.subheader("Gasto en sanidad (% del PIB)")
  recursos_sanidad = {
    'Pais': ['EE.UU.','Suiza','Alemania','Francia','Suecia','Canada','Dinamarca','Portugal','Chile','España','Italia','Corea del sur','Grecia','Polonia','Letonia','Mexico','luxemburgo','Turquia'],
    '% del PIB': [16.9,12.2,11.2,11.2,11,10.7,10.5,9.1,8.9,8.9,8.8,8.1,7.8,6.3,5.9,5.5,5.4,4.2]
    }
  df = pd.DataFrame(recursos_sanidad)
  fig = px.bar(df,x='Pais',y='% del PIB')
  fig
  df
  st.write("La desigualdad en los indicadores es reflejo de la desigualdad en la acción pública, ya que el gasto público en salud no es progresivo y ha mantenido a cerca de 50% de la población fuera de los sistemas de seguridad pública.")
  st.subheader("Principales causas de mortalidad")
  mortalidad_causas = {
    'Causa': ['Enfermedad del corazon','Diabetes mellitus','Tumores malignos','Enfermedades del higado','Agresiones','Enfermedades cerebrovasculares'],
    'Número de defunciones': [156041,104352,88682,40578,36661,35303]
  }
  df1 = pd.DataFrame(mortalidad_causas)
  fig = px.bar(df1,x='Causa',y='Número de defunciones')
  fig
