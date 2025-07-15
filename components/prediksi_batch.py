import streamlit as st
import pandas as pd

def preprocess_input(data):
    return pd.DataFrame([data]) if isinstance(data, dict) else data

def prediksi_batch(transformer, model, scaler_y, simpan_ke_supabase, classify_clv):
    st.subheader("Upload File CSV")

    st.markdown("""
    **📌 Format Kolom CSV yang Diperlukan:**
    File CSV yang diunggah harus memiliki kolom berikut:

    ```
    Months Since Last Claim, Months Since Policy Inception, Number of Policies,
    Number of Open Complaints, Monthly Premium Auto, Total Claim Amount, Income,
    Education, Gender, Marital Status, EmploymentStatus, Location Code, State,
    Coverage, Policy Type, Policy, Renew Offer Type, Sales Channel, Vehicle Class,
    Vehicle Size
    ```
    """)

    file = st.file_uploader("Upload file CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        X = transformer.transform(preprocess_input(df))
        y_pred_scaled = model.predict(X)
        y_preds = scaler_y.inverse_transform(y_pred_scaled).flatten()
        df['Predicted_CLV'] = y_preds
        df['CLV_Category'] = df['Predicted_CLV'].apply(classify_clv)
        st.dataframe(df)

        for _, row in df.iterrows():
            simpan_ke_supabase(row.to_dict(), row['Predicted_CLV'], row['CLV_Category'])
