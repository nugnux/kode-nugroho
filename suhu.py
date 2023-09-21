import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
    x = st.number_input('suhu ',value=100)
with c2:
    satuan = st.selectbox(
        'satuan',
        ('C', 'F', 'R','K'))



st.caption('Copyright © Nugroho Adi Pramono 2023')
