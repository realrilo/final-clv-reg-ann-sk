import streamlit as st
from PIL import Image

def info_model():
    st.header("Informasi Model")

    st.markdown("""
        Model ini menggunakan pendekatan **Artificial Neural Network (ANN)** untuk memprediksi Customer Lifetime Value (CLV).
        Model ini dilatih menggunakan data pelanggan yang mencakup informasi demografis, transaksi, dan polis asuransi.
    """)

    # ========================== 1. LOSS =============================
    st.subheader("Hasil Pelatihan Model")

    col1, col2 = st.columns([1, 1])
    with col1:
        image = Image.open("images/loss_plot.png")
        st.image(image, caption="Training vs Validation Loss", use_column_width=True)

    with col2:
        st.markdown("""
        **Training vs Validation Loss**  
        Grafik ini menunjukkan penurunan nilai *Mean Squared Error (MSE)* pada data latih dan validasi selama 200 epoch.  
        - **Training Loss (biru)** menurun drastis dan terus membaik mendekati nol.  
        - **Validation Loss (oranye)** menurun awalnya, kemudian stagnan.  
        - Selisih yang cukup lebar menunjukkan potensi *underfitting ringan*, namun tidak terjadi *overfitting*.  
        """)

    # ======================= 2. ARSITEKTUR ==========================
    st.subheader("Arsitektur Model")

    col3, col4 = st.columns([1, 1])
    with col3:
        image = Image.open("images/arsitektur_model.png")
        st.image(image, caption="Struktur Model ANN", use_column_width=True)

    with col4:
        st.markdown("""
        **Arsitektur Model ANN**  
        Model Artificial Neural Network (ANN) dibangun dengan:  
        - Beberapa *hidden layer* (misalnya: 128 → 64 → 32 neuron).  
        - Aktivasi: **ReLU** pada hidden layer dan **linear** pada output.  
        - Optimizer: **Adam**  
        - Loss Function: **Mean Squared Error (MSE)**  
        Struktur ini memungkinkan model menangkap pola non-linear pada data CLV.  
        """)

    # ======================== 3. PREDIKSI ===========================
    st.subheader("Prediksi CLV")

    col5, col6 = st.columns([1, 1])
    with col5:
        image = Image.open("images/pred_aktual.png")
        st.image(image, caption="Perbandingan Nilai Prediksi vs Aktual", use_column_width=True)

    with col6:
        st.markdown("""
        **Perbandingan Nilai Prediksi vs Aktual CLV**  
        Grafik ini menampilkan sebaran nilai prediksi model terhadap nilai aktual CLV.  
        - Titik-titik biru mewakili prediksi per data pelanggan.  
        - Garis merah putus-putus adalah garis ideal (prediksi = aktual).  
        - Sebagian besar prediksi dekat garis tersebut → model cukup akurat.  
        - Terdapat *outlier* yang mengindikasikan beberapa data sulit dipelajari model.  
        """)

