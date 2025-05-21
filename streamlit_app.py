
import streamlit as st

st.title("🎈 pacarjisung")
st.write(
  "ayoo main bersama pacar jisung,"
)
st.image("jisung_ratio-16x9.jpg", width=800)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
   st.write("f{angka} adalah Bilangan Genap")
else
   st.write("f{angka} adalah Bilangan Ganjil")
