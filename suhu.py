import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

option = st.selectbox(
    'satuan',
    ('C', 'F', 'R','K'))

f1 = st.number_input('f1 = ',value=1)


st.caption('Copyright © Nugroho Adi Pramono 2023')
