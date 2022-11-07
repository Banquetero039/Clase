import streamlit as st
st.title('Aplicacion para...')
st.image("https://www.limarp.com/img/obesidad-morbida.png")
st.sidebar.header("¿Que estado tiene mayor porcentaje de obesidad?")
with st.sidebar:
  porcentaje = st.radio("Estados:",("Baja california sur","Tabasco","Distrito federal"))
  if porcentaje == "Baja california":
    st.write("80%")
  
  estatura = st.number_input("Ingresa tu estatura en metros",)
  st.write(estatura)
  
  masa = st.number_input("Ingresa tu masa en Kg")
  st.write(masa)
  
  imc = masa/estatura**2
  st.write(imc)
import streamlit as st
st.write('''
# This is the document title
This is some_markdown_.
''')
import pandas as pd
df = pd.DataFrame({'Col1':[1,2,3],'Col2':[4,5,6]})
st.write(df)
texto = st.text_area('Problematica', '''
    
    ''')
st.button("IMC")
