import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model/model.pkl", "rb"))

st.set_page_config(layout="wide")

st.title("🏠 Real Estate Price Predictor")
st.caption("Strict Rule-Based ML Model (BHK + City + Area)")

st.divider()

col1, col2, col3 = st.columns([1,2,1])

with col2:

    bedrooms = st.selectbox("Bedrooms (BHK)", [1,2,3])
    bathrooms = st.selectbox("Bathrooms", [1,2,3])

    if bedrooms == 1:
        area = st.slider("Area (sq ft)", 600, 800, 700)
    elif bedrooms == 2:
        area = st.slider("Area (sq ft)", 800, 1200, 1000)
    else:
        area = st.slider("Area (sq ft)", 1200, 1500, 1350)

    location = st.selectbox("City", [
        "Mumbai","Pune","Noida",
        "Bhopal","Indore","Jabalpur",
        "Rewa","Satna","Sagar"
    ])

    if st.button("🔮 Predict Price"):

        if location in ["Mumbai","Pune","Noida"]:
            city_score = 2
        elif location in ["Bhopal","Indore","Jabalpur"]:
            city_score = 1
        else:
            city_score = 0

        input_data = np.array([[
            area, bedrooms, bathrooms, city_score
        ]])

        prediction = model.predict(input_data)[0]

        if prediction >= 10000000:
            price = f"₹ {prediction/10000000:.2f} Cr"
        elif prediction >= 100000:
            price = f"₹ {prediction/100000:.2f} L"
        else:
            price = f"₹ {prediction:,.0f}"

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            padding: 65px;
            border-radius: 22px;
            text-align: center;
            color: white;
            margin-top: 30px;
        ">
            <h2>Estimated Market Value</h2>
            <h1 style="font-size:62px;">{price}</h1>
        </div>
        """, unsafe_allow_html=True)