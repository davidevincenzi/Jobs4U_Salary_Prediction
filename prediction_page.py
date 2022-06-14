import streamlit as st
import pickle
import numpy as np

data = pickle.load(open("saved_steps.pkl", "rb"))

regressor = data["model"]
le_education = data["lbl_education"]
le_country = data["lbl_country"]

def show_prediction_page():
    st.title("Jobs4U Salary Prediction")
    st.write("""### Use our tool to predict your salary""")

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    countries = (
        "United States of America",
        "India",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway"
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Predict Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
