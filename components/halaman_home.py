import streamlit as st
import pandas as pd

# --- Halaman 1: Home ---
def halaman_home():
    """Menampilkan konten untuk halaman Home."""
    st.title("🏠 Selamat Datang di Aplikasi Prediksi CLV")
    st.markdown("Selamat datang di dasbor Analisis **Customer Lifetime Value (CLV)**. Aplikasi ini dirancang untuk membantu Anda memahami dan memprediksi nilai dari setiap pelanggan selama mereka menjalin hubungan dengan bisnis Anda.")
    
    st.header("Apa itu Customer Lifetime Value (CLV)?")
    st.markdown("""
    **Customer Lifetime Value (CLV)** atau **Nilai Seumur Hidup Pelanggan** adalah metrik yang memprediksi **total keuntungan** yang bisa didapat dari seorang pelanggan selama mereka masih menjadi pelanggan Anda. Metrik ini tidak hanya melihat pembelian pertama, tetapi keseluruhan potensi pendapatan di masa depan.
    """)
    
    st.header("Mengapa CLV Penting?")
    st.markdown("""
    - **Meningkatkan Profitabilitas**: Fokus pada pelanggan yang paling menguntungkan.
    - **Meningkatkan Retensi**: Rancang program loyalitas untuk mempertahankan pelanggan bernilai tinggi.
    - **Optimalisasi Pemasaran**: Tentukan biaya yang layak untuk mendapatkan pelanggan baru.
    - **Segmentasi Lebih Baik**: Kelompokkan pelanggan untuk penawaran yang lebih personal.
    """)

    st.header("Fitur Aplikasi Ini")
    st.markdown("""
    - **Prediksi CLV**: Lakukan prediksi nilai pelanggan secara *real-time* (Online) atau massal (*Batch*).
    - **Riwayat Prediksi**: Lihat dan kelola semua riwayat prediksi yang pernah Anda lakukan.
    - **Informasi Model**: Pahami model dan metrik yang digunakan dalam aplikasi ini.
    """)