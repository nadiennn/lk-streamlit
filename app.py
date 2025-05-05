import streamlit as st

#Menambahkan judul
st.title("mulai telusuri")

#menambahkan header
st.header('Introducing')
st.write('haii manteman terima kasih telah menggunakan layanan web aku, terlebih dahulu perkenalkan nama aku nadien, disini tujuan aku membuat web ini agar dapat membantu kalian mencari sesuatu dengan mudah')

#Menambahkan subheader (tulisannya lebih kecil dari header)
st.subheader('laman web')

#Menambahkan caption (tulisan kecil yang tidak terlalu mencolok)
st.caption('seperti judul sebelumnya ini laman web')

#Mendemonstrasikan kode
st.code('import streamlit as st')
st.text('Ini adalah teks penting yang harus di ketik untuk mendapatkan tampilan seperti yang tertera di layar anda.')

#Menampilkan rumus
st.latex(r' y = mx + b ')
st.text("Code yang dipakai untuk menampilkan rumus seperti di atas adalah (r' y = mx + b ')")

#Mengubah tebal, miring, gambar, tautan, and other
st.markdown('**Link** dan _link_ serta [Tautan](https://streamlit.io)')

import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Data Mahasiswa")

# Garis pemisah pertama
st.divider()

# Data
data = {
    'Nama': ['nadien', 'kale', 'abel'],
    'Usia': ['19', '22', '23'],
    'Asal Daerah': ['palopo', 'batam', 'bandung']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Berikut adalah data mahasiswa:")
st.dataframe(df)

# Garis pemisah kedua (opsional)
st.divider()

#Menampilkan file metric
st.metric(label="Total Penjualan", value=2500, delta="+330")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 225 juta", delta="+8%")
with col2:
    st.metric(label="User Aktif", value="1.260", delta="+2%")
with col3:
    st.metric(label="Refund", value="17", delta="-1%")

col1, col2 = st.columns(2)
st.divider()

#Menampilkan grafik
import numpy as np
import streamlit as st

#Line Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

#Bar Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.bar_chart(data)

#altair chart
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

#map
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.map()

#contoh mini semua input
import streamlit as st

with st.form("form_input"):
    nama = st.text_input("nadien")
    alamat = st.text_area("palopo")
    usia = st.number_input("19", min_value=0)
    tanggal_lahir = st.date_input("11 april 2006")
    waktu_janji = st.time_input("20.30")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Mambaca", "cooking", "Musik", "Traveling"])
    warna_favorit = st.color_picker("green and puprle")
    file_foto = st.file_uploader("Upload foto")
    foto_kamera = st.camera_input("Ambil foto dari kamera")
    rating = st.slider("Rating kepuasan", 1, 10)

    submitted = st.form_submit_button("Done Bro")

if submitted:
    st.success(f"Data {nama} berhasil dikirim! {"Tanggal"}")

    #Menampilkan Gambar
import streamlit as st
from PIL import Image

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg",
    caption="fun fact nya tau mona lisa dari penyanyi alfie castley dengan judul lagu teenage mona lisa",
    use_container_width=True
)

#Menampilkan video dari file lokal
st.video('vidio nadien.mp4')

st.title("Data Karyawan")
st.dataframe(df)















