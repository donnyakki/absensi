import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Dashboard Absensi", layout="wide")

st.title("📊 Upload Absensi GreatDay")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write("Preview Data:", df.head())

    # Normalisasi kolom (biar fleksibel)
    df.columns = df.columns.str.lower().str.strip()

    conn = get_connection()
    cur = conn.cursor()

    for i, row in df.iterrows():
        cur.execute("""
            INSERT INTO absensi 
            (nama, nik, tanggal, jam_masuk, jam_keluar, status, lokasi, unit)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row.get('nama'),
            row.get('nik'),
            row.get('tanggal'),
            row.get('jam masuk'),
            row.get('jam keluar'),
            row.get('status'),
            row.get('lokasi'),
            row.get('unit')
        ))

    conn.commit()
    cur.close()
    conn.close()

    st.success("✅ Data berhasil diupload ke database!")
