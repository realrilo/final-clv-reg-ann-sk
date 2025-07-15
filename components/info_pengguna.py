import streamlit as st

def info_pengguna():
    st.header("Daftar Fitur Model")
    st.markdown("""
        ### Penjelasan Fitur Model CLV

        #### 1. **Months Since Last Claim**
        - **Deskripsi**: Jumlah bulan sejak pelanggan terakhir mengajukan klaim.
        - **Tipe**: Numerik
        - **Rentang Umum**: 0 – 50+

        #### 2. **Months Since Policy Inception**
        - **Deskripsi**: Jumlah bulan sejak pelanggan memulai polis asuransinya.
            - **Tipe**: Numerik
            - **Rentang Umum**: 0 – 100+

            #### 3. **Number of Policies**
            - **Deskripsi**: Jumlah polis atau kontrak asuransi aktif yang dimiliki pelanggan.
            - **Tipe**: Numerik
            - **Rentang Umum**: 1 – 9

            #### 4. **Number of Open Complaints**
            - **Deskripsi**: Jumlah keluhan aktif atau terbuka yang diajukan oleh pelanggan.
            - **Tipe**: Numerik
            - **Rentang Umum**: 0 – 5

            #### 5. **Monthly Premium Auto**
            - **Deskripsi**: Jumlah premi asuransi kendaraan yang dibayar pelanggan setiap bulan.
            - **Tipe**: Numerik
            - **Rentang Umum**: 0 – 300+

            #### 6. **Total Claim Amount**
            - **Deskripsi**: Total nilai klaim yang diajukan oleh pelanggan.
            - **Tipe**: Numerik
            - **Rentang Umum**: 0 – 8000+

            #### 7. **Income**
            - **Deskripsi**: Pendapatan tahunan pelanggan dalam satuan dolar.
            - **Tipe**: Numerik
            - **Rentang Umum**: 0 – 250000

            ---

            ### Fitur Kategorikal

            #### 8. **Education**
            - **Deskripsi**: Tingkat pendidikan terakhir pelanggan.
            - **Pilihan**:
            - High School or Below
            - College
            - Bachelor
            - Master
            - Doctor

            #### 9. **Gender**
            - **Deskripsi**: Jenis kelamin pelanggan.
            - **Pilihan**:
            - Male
            - Female

            #### 10. **Marital Status**
            - **Deskripsi**: Status pernikahan pelanggan.
            - **Pilihan**:
            - Married
            - Single
            - Divorced

            #### 11. **EmploymentStatus**
            - **Deskripsi**: Status pekerjaan pelanggan.
            - **Pilihan**:
            - Employed
            - Unemployed
            - Medical Leave
            - Disabled
            - Retired

            #### 12. **Location Code**
            - **Deskripsi**: Kategori wilayah tempat tinggal pelanggan.
            - **Pilihan**:
            - Urban: Wilayah perkotaan
            - Suburban: Wilayah pinggiran kota
            - Rural: Wilayah pedesaan

            #### 13. **State**
            - **Deskripsi**: Negara bagian tempat tinggal pelanggan.
            - **Pilihan**:
            - California
            - Oregon
            - Washington
            - Nevada
            - Arizona

            #### 14. **Coverage**
            - **Deskripsi**: Tingkat perlindungan asuransi yang dipilih.
            - **Pilihan**:
            - Basic: Perlindungan dasar
            - Extended: Perlindungan tambahan
            - Premium: Perlindungan maksimal

            #### 15. **Policy Type**
            - **Deskripsi**: Tipe polis berdasarkan kepemilikan kendaraan.
            - **Pilihan**:
            - Personal Auto
            - Corporate Auto
            - Special Auto

            #### 16. **Policy**
            - **Deskripsi**: Paket detail dari polis yang menggabungkan tipe kendaraan dan tingkat perlindungan.
            - **Format**: [Policy Type] + [Level]
            - **Pilihan**:
            - Personal L1, L2, L3
            - Corporate L1, L2, L3
            - Special L1, L2, L3
            - **Penjelasan Level**:
            - **L1**: Perlindungan dasar
            - **L2**: Perlindungan menengah
            - **L3**: Perlindungan lengkap
            - **Contoh**:
            - *Personal L3*: Polis individu dengan perlindungan lengkap.
            - *Corporate L1*: Untuk kendaraan perusahaan, perlindungan minimal.
                                
            #### 17. **Renew Offer Type**
            - **Deskripsi**: Tipe penawaran perpanjangan polis yang diberikan kepada pelanggan saat masa polis hampir berakhir.
            - **Pilihan**:
            - **Offer1**: Penawaran standar tanpa diskon
            - **Offer2**: Diskon kecil
            - **Offer3**: Penambahan manfaat tertentu
            - **Offer4**: Penawaran terbaik, diskon besar atau bonus
            - **Tujuan**: Meningkatkan kemungkinan pelanggan memperpanjang polis.

            #### 18. **Sales Channel**
            - **Deskripsi**: Kanal atau media tempat pelanggan membeli asuransi.
            - **Pilihan**:
            - Agent: Lewat agen langsung
            - Call Center
            - Web: Melalui situs web
            - Branch: Cabang fisik

            #### 19. **Vehicle Class**
            - **Deskripsi**: Jenis kendaraan yang diasuransikan.
            - **Pilihan**:
            - Two-Door Car
            - Four-Door Car
            - SUV
            - Luxury Car
            - Luxury SUV
            - Sports Car

            #### 20. **Vehicle Size**
            - **Deskripsi**: Ukuran fisik kendaraan.
            - **Pilihan**:
            - Small: Kendaraan kecil (misalnya city car)
            - Medsize: Ukuran sedang (misalnya sedan)
            - Large: Ukuran besar (misalnya SUV besar atau van)

            ---

            ### Catatan
            - Semua nilai numerik sebaiknya dimasukkan dalam rentang wajar seperti di atas.
            - Untuk input kategorikal, pilih sesuai dengan pilihan yang tersedia agar prediksi akurat.
            """)   