import streamlit as st
import pandas as pd
import tensorflow as tf
import pickle
from datetime import datetime
from PIL import Image
from supabase import create_client, Client
import os
import json
from dotenv import load_dotenv
from streamlit_modal import Modal
from streamlit_option_menu import option_menu

# Load .env file
load_dotenv()

# === Konfigurasi Supabase ===
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# === Load Model dan Preprocessing ===
model = tf.keras.models.load_model('model/model_clv.h5')
with open('model/transformer.pkl', 'rb') as f:
    transformer = pickle.load(f)
with open('model/scaler_y.pkl', 'rb') as f:
    scaler_y = pickle.load(f)

# === Fungsi-fungsi ===
def preprocess_input(data):
    return pd.DataFrame([data]) if isinstance(data, dict) else data


def classify_clv(value):
    if value >= 8962:
        return "High Value"
    elif value >= 5780:
        return "Medium Value"
    else:
        return "Low Value"

def simpan_ke_supabase(input_data, predicted_clv, clv_category):
    timestamp = datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "input_data": json.dumps(input_data),
        "predicted_clv": float(predicted_clv),
        "clv_category": clv_category
    }
    supabase.table("clv_history").insert(data).execute()


def tampilkan_riwayat():
    st.subheader("Riwayat Prediksi CLV")

    # --- Bagian 1: Inisialisasi Modal dan Session State ---
    # Definisikan SATU modal saja di luar perulangan
    modal = Modal("Konfirmasi Penghapusan", key="modal_hapus_satu", max_width=450)

    # Inisialisasi session_state untuk menyimpan ID yang akan dihapus
    if 'id_to_delete' not in st.session_state:
        st.session_state.id_to_delete = None

    # --- Bagian 2: Tampilkan Data dengan Tombol ---
    result = supabase.table("clv_history").select("*").order("timestamp", desc=True).execute()
    records = result.data if result.data else []

    if not records:
        st.info("Belum ada riwayat prediksi.")
        return

    # Loop untuk menampilkan setiap baris riwayat
    for row in records:
        with st.container(border=True):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"**ID:** {row['id']} | **Waktu:** {row['timestamp']}")
                st.write(f"**Input:** {row['input_data']}")
                st.write(f"**Prediksi CLV:** ${row['predicted_clv']:,.2f}")
                st.write(f"**Kategori:** {row['clv_category']}")
            
            with col2:
                # Tombol ini sekarang hanya bertugas menyimpan ID dan membuka modal
                if st.button("🗑️ Hapus", key=f"hapus_{row['id']}"):
                    st.session_state.id_to_delete = row['id']
                    modal.open()

    # --- Bagian 3: Logika Modal (di luar perulangan) ---
    # Logika ini hanya berjalan jika modal sedang terbuka
    if modal.is_open():
        with modal.container():
            st.error(f"Anda yakin ingin menghapus riwayat dengan ID {st.session_state.id_to_delete}?")
            st.write("Tindakan ini tidak dapat dibatalkan.")
            
            # Tombol konfirmasi di dalam modal
            if st.button("Ya, Hapus Permanen", key="confirm_hapus"):
                # Ambil ID dari session_state untuk dihapus
                supabase.table("clv_history").delete().eq("id", st.session_state.id_to_delete).execute()
                st.success(f"Riwayat ID {st.session_state.id_to_delete} telah dihapus.")
                
                # Reset state dan tutup modal
                st.session_state.id_to_delete = None
                modal.close()
                st.rerun()
            
            if st.button("Batal", key="batal_hapus"):
                # Cukup reset state dan tutup modal
                st.session_state.id_to_delete = None
                modal.close()

    st.divider()

    # --- Bagian untuk Hapus Semua Riwayat ---
    # Definisikan modal untuk hapus semua
    modal_all = Modal(
        "Konfirmasi Hapus Seluruh Riwayat", 
        key="modal_all",
        max_width=450
    )

    # Tombol untuk membuka modal hapus semua
    if st.button("🗑️ Hapus Semua Riwayat", type="primary"):
        modal_all.open()

    # Logika di dalam modal hapus semua
    if modal_all.is_open():
        with modal_all.container():
            st.error("Anda yakin ingin menghapus SELURUH riwayat prediksi?")
            st.warning("Tindakan ini akan menghapus semua data dan tidak dapat dibatalkan.")
            
            if st.button("Ya, Saya Mengerti dan Ingin Menghapus Semua"):
                supabase.table("clv_history").delete().neq("id", 0).execute()
                st.success("Seluruh riwayat berhasil dihapus.")
                modal_all.close()
                st.rerun()
            
            if st.button("Batal Hapus Semua"):
                modal_all.close()

# === Aplikasi Utama ===
def main():
    st.set_page_config(page_title="Prediksi CLV", layout="wide")

    # --- NAVIGASI SIDEBAR DENGAN GAYA TAB ---
    with st.sidebar:
        # st.image(...) # Anda bisa letakkan gambar di sini

        # Atur navigasi dan jadikan "Home" sebagai default (default_index=0)
        pilihan = option_menu(
            menu_title="Menu Utama",
            options=["Home", "Prediksi", "Riwayat Prediksi", "Informasi Pengguna", "Informasi Model"],
            icons=["house-door", "cpu", "clock-history", "person-badge", "archive"], # Tambahkan ikon untuk Home
            menu_icon="cast",
            default_index=0 # <-- INI KUNCINYA: Mengatur "Home" sebagai halaman default
        )
        
        # Sub-menu hanya muncul jika di halaman "Prediksi"
        prediksi_mode = None
        if pilihan == "Prediksi":
            prediksi_mode = option_menu(
                menu_title="Mode Prediksi",
                options=["Online", "Batch"],
                icons=["person-fill", "people-fill"],
                menu_icon="gear-wide-connected",
                orientation="horizontal"
            )

        

    # --- KONTEN HALAMAN UTAMA (Logika Pemanggilan Halaman) ---
    if pilihan == "Home":
        from components.halaman_home import halaman_home
        halaman_home()
    elif pilihan == "Prediksi":
        st.title("Prediksi Customer Lifetime Value (CLV)")
        if prediksi_mode == "Online":
            from components.prediksi_online import prediksi_online
            prediksi_online(transformer, model, scaler_y, simpan_ke_supabase)
        elif prediksi_mode == "Batch":
            from components.prediksi_batch import prediksi_batch
            prediksi_batch(transformer, model, scaler_y, simpan_ke_supabase, classify_clv)

    elif pilihan == "Riwayat Prediksi":
        tampilkan_riwayat()

    elif pilihan == "Informasi Pengguna":
        from components.info_pengguna import info_pengguna
        info_pengguna()

    elif pilihan == "Informasi Model":
        from components.info_model import info_model
        info_model()

if __name__ == "__main__":
    main()