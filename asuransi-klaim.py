import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('data_claim_asuransi.sav', 'rb'))

#judul web
st.title('Prediksi Data Klaim Asuransi')


col1, col2,  = st.columns(2)

st.text ('Renaldi Al Anshari , 191351075')
with col1 :
    age = st.number_input('Usia')
with col2 :
    sex = st.number_input('Jenis Kelamin')
with col1 :
    bmi = st.number_input('Index Massa Tubuh')
with col2 :
    steps = st.number_input('rata-rata langkah berjalan per hari pemegang polis')
with col1 :
    children = st.number_input('Jumlah Anak')
with col2 :
    smoker = st.number_input('Status Merokok Pemegang Polis')
with col1 :
    region = st.number_input('Wilayah Tempat Tinggal Pemegang Polis di AS')
with col2 :
    charges = st.number_input('biaya medis individu yang ditagih oleh asuransi kesehatan')
# code for prediction
klaim_asuransi_data =''

# membuat tombol prediksi 
if st.button('Prediksi Data Klaim Asuransi'):
    klaim_asuransi_prediction = model.predict([[age, sex, bmi, steps, children, smoker, region, charges]])

    if (klaim_asuransi_prediction[0]==1):
        klaim_asuransi_data = 'Mendapat Hak Klaim Asuransi'
    else :
        klaim_asuransi_data = 'Tidak Mendapat Hak Klaim Asuransi'
st.success(klaim_asuransi_data)