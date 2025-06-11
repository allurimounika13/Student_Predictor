import streamlit as st
from predictor import predict_colleges
st.set_page_config(page_title="Student College Predictor", layout="wide")

st.title("🎓 TS EAMCET Student College Predictor")

# Input fields
name = st.text_input("👤 Student Name")
rank = st.number_input("📊 EAMCET Rank", min_value=1, step=1)
category = st.selectbox("🏷️ Category", ["OC", "BC_A", "BC_B", "BC_C", "BC_D", "BC_E", "SC", "ST", "EWS"])
gender = st.radio("🚻 Gender", ["BOYS", "GIRLS"])

# Predict button
if st.button("🔍 Predict Colleges"):
    if not name.strip():
        st.warning("Please enter the student's name.")
    else:
        results = predict_colleges(rank, category, gender)

        if results.empty:
            st.error("❌ No eligible colleges found for the given details.")
        else:
            st.success(f"✅ Found {len(results)} colleges for {name}!")
            st.dataframe(results, use_container_width=True)
