import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

if(satuan=='C'):
    if(konversi=='C'):
        y = x
    elif(kenversi=='F'):
        y = x * 9/5 + 32 
with c1:
    x = st.number_input('Suhu ',value=100)
    st.write('Dikonversi ke: ')
with c2:
    satuan = st.selectbox(
        'Satuan',
        ('C', 'F', 'R','K'),key='k1')
    konversi = st.selectbox(
        'Konversi',
        ('C', 'F', 'R','K'),key='k2') 

st.write(x,' ',satuan,' = ',konversi)



st.caption('Copyright © Nugroho Adi Pramono 2023')
