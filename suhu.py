import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')


x = st.number_input('suhu ',value=100)
satuan = st.selectbox(
    'satuan',
    ('C', 'F', 'R','K'))



st.caption('Copyright © Nugroho Adi Pramono 2023')
