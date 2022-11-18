import streamlit as st
import pandas as pd
import numpy as np
import os, time
import plotly.express as px

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
  st.subheader("‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ Diabetes‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ")
  st.write("La diabetes es una enfermedad crónica (de larga duración) que afecta la forma en que el cuerpo convierte los alimentos en energía.")
  st.write("Su cuerpo descompone la mayor parte de los alimentos que come en azúcar (también llamada glucosa) y los libera en el torrente sanguíneo.")
  st.subheader("‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Presion arterial alta‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ")
  st.write("La presión arterial es la fuerza de su sangre al empujar contra las paredes de sus arterias. Cada vez que su corazón late, bombea sangre hacia las arterias. Su presión arterial es más alta cuando su corazón late, bombeando la sangre. Esto se llama presión sistólica. Cuando su corazón está en reposo, entre latidos, su presión arterial baja. Esto se llama presión diastólica.")
  st.image("https://www.mayoclinic.org/-/media/kcms/gbs/patient-consumer/images/2018/05/11/14/58/blood-pressure-monitor-8col-3559308-001-0.jpg")
  st.subheader("‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ Enfermedad Coronaria ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ")
  st.write("La obesidad es un factor de riesgo para la enfermedad coronaria, que es causada por la acumulacion de placa de colesterol en las arterias del corazon. Otras enfermedades tambien vinculadas con esta enfermedad la obesidad es la mas comun. El riesgo de la CAD es mayor en personas con obesidad central o visceral que se concentra en el abdomen.")
  st.image("https://www.topdoctors.mx/files/Image/large/bb432106d09ddc88886827a8bcf5f052.jpg")
  
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
if opciones =="Soluciones":
  st.title("Las soluciones")
  st.subheader("Mejor alimentación, menos productos procesados y más actividad fisica.")
  st.write("Más del 95% de los casos de obesidad infantil se deben a dietas con alto valor calórico y a baja actividad fisica, por lo que el sobrepeso y la obesidad pueden prevenirse en la mayoria de las niñas y niños mejorando sus habitos de nutricion y salud, y promoviendo una mayor actividad fisica.")
  
  st.write("• Niñas, niños y adolescentes construyan hábitos de consumo de alimentos saludables.")
  st.write("• Las familias más vulnerables cuenten con los recursos para adquirir alimentos suficientes y nutritivos.")
  st.write("• Se reduzca el consumo de bebidas azucaradas y alimentos ultra procesados, altos en grasas, sodio y azúcares.")
  st.write("• Niños, niñas y adolescentes construyan hábitos con mayor actividad física y menos sedentarismo.")
  st.image("https://img.freepik.com/vector-premium/deporte-fitness-vida-sana-diseno_24877-14801.jpg?w=2000")
  
  st.header("¿Cómo saber si tu nivel de azucar en la sangre esta en un buen nivel y si estas en riesgo de tener diabetes?")
  
  st.subheader("Tu valor de azucar en la sangre:")
  x = st.slider("Número entre 40-500",
                min_value=40, max_value=500, step=1)
  st.write("Tu valor:", x)
  
  st.subheader("Tu edad:")
  y = st.slider("Que edad tienes?",
                min_value=0, max_value=100, step=1)
  st.write("Tu edad:", y)
  if x == 40:
    st.write("Peligro coma diabetico👩‍⚕️️💉📅")
with st.sidebar:
  st.image("https://blogsaverroes.juntadeandalucia.es/habitosdevidasaludables/files/2020/05/images.jpg")
with st.sidebar:
  st.write("Mayte Fabiola Navarro Barrios 348934")
with st.sidebar:
  st.write("Ariana Guadalupe Negrete Morales 355429")
with st.sidebar:
  st.write("Ana Sofia Amado Urias 349143")
with st.sidebar:
  st.write("Luis Angel Ramirez Trejo 345545")
  
