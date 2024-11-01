import streamlit as st

# Judul Aplikasi
st.title("Contoh Aplikasi Streamlit")

# Input dari pengguna
nama = st.text_input("Masukkan Nama Anda:")
umur = st.slider("Masukkan Umur Anda:", 1, 100)

# Menampilkan output
st.write(f"Halo, {nama}! Umur Anda adalah {umur} tahun.")