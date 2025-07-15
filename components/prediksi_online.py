import streamlit as st
import pandas as pd

def preprocess_input(data):
    return pd.DataFrame([data]) if isinstance(data, dict) else data

def prediksi_online(transformer, model, scaler_y, simpan_ke_supabase):
    st.subheader("Masukkan Data Pelanggan")
    col1, col2, col3 = st.columns(3)
    with col1:
        mslc = st.number_input("Months Since Last Claim", min_value=0, value=5)
        nop = st.number_input("Number of Policies", min_value=1, value=1)
        income = st.number_input("Income", min_value=0, value=50000)
        education = st.selectbox("Education", ['Bachelor', 'College', 'Master', 'High School or Below', 'Doctor'])
    with col2:
        mspi = st.number_input("Months Since Policy Inception", min_value=0, value=24)
        nooc = st.number_input("Number of Open Complaints", min_value=0, value=0)
        gender = st.selectbox("Gender", ['Male', 'Female'])
        marital = st.selectbox("Marital Status", ['Married', 'Single', 'Divorced'])
    with col3:
        premium = st.number_input("Monthly Premium Auto", min_value=0, value=100)
        claim = st.number_input("Total Claim Amount", min_value=0.0, value=300.0)
        emp_status = st.selectbox("Employment Status", ['Employed', 'Unemployed', 'Medical Leave', 'Disabled', 'Retired'])
        location = st.selectbox("Location Code", ['Urban', 'Suburban', 'Rural'])

    col4, col5, col6 = st.columns(3)
    with col4:
        state = st.selectbox("State", ['Washington', 'Arizona', 'Nevada', 'California', 'Oregon'])
        coverage = st.selectbox("Coverage", ['Basic', 'Extended', 'Premium'])
        policy_type = st.selectbox("Policy Type", ['Personal Auto', 'Corporate Auto', 'Special Auto'])
    with col5:
        policy = st.selectbox("Policy", ['Personal L3', 'Personal L2', 'Personal L1',
                                         'Corporate L3', 'Corporate L2', 'Corporate L1',
                                         'Special L3', 'Special L2', 'Special L1'])
        renew = st.selectbox("Renew Offer Type", ['Offer1', 'Offer2', 'Offer3', 'Offer4'])
        channel = st.selectbox("Sales Channel", ['Agent', 'Call Center', 'Web', 'Branch'])
    with col6:
        vehicle_class = st.selectbox("Vehicle Class", ['Two-Door Car', 'Four-Door Car', 'SUV', 'Luxury Car', 'Luxury SUV', 'Sports Car'])
        vehicle_size = st.selectbox("Vehicle Size", ['Small', 'Medsize', 'Large'])

    input_data = {
        'Months Since Last Claim': mslc,
        'Months Since Policy Inception': mspi,
        'Number of Policies': nop,
        'Number of Open Complaints': nooc,
        'Monthly Premium Auto': premium,
        'Total Claim Amount': claim,
        'Income': income,
        'Education': education,
        'Gender': gender,
        'Marital Status': marital,
        'EmploymentStatus': emp_status,
        'Location Code': location,
        'State': state,
        'Coverage': coverage,
        'Policy Type': policy_type,
        'Policy': policy,
        'Renew Offer Type': renew,
        'Sales Channel': channel,
        'Vehicle Class': vehicle_class,
        'Vehicle Size': vehicle_size
    }

    if st.button("Prediksi"):
        X = transformer.transform(preprocess_input(input_data))
        y_scaled = model.predict(X)
        y_pred = scaler_y.inverse_transform(y_scaled)[0][0]

        kategori = "High Value" if y_pred >= 8962 else "Medium Value" if y_pred >= 5780 else "Low Value"
        st.success(f"CLV: ${y_pred:,.2f}")
        st.info(f"Kategori Pelanggan: **{kategori}**")

        simpan_ke_supabase(input_data, y_pred, kategori)
