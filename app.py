
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Încărcăm modelul și lista de variabile
model = joblib.load('data/final_movie_flop_model.pkl')
features_app = joblib.load('data/features_app.pkl')

st.set_page_config(
    page_title="Movie Flop Predictor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Flop Predictor")
st.write("""
Această aplicație estimează performanța financiară relativă a unui film,
folosind modelul final Gradient Boosting optimizat.
""")

st.markdown("---")

st.subheader("Introduceți caracteristicile filmului")

budget = st.number_input(
    "Buget film ($)",
    min_value=100000,
    max_value=500000000,
    value=100000000,
    step=1000000
)

vote_average = st.slider(
    "Rating mediu",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

vote_count = st.number_input(
    "Număr voturi",
    min_value=0,
    max_value=50000,
    value=5000,
    step=100
)

popularity = st.number_input(
    "Popularitate",
    min_value=0.0,
    max_value=1000.0,
    value=80.0,
    step=1.0
)

runtime = st.number_input(
    "Durată film (minute)",
    min_value=30,
    max_value=300,
    value=120,
    step=5
)

release_year = st.number_input(
    "An lansare",
    min_value=1950,
    max_value=2026,
    value=2025,
    step=1
)

release_month = st.selectbox(
    "Luna lansării",
    options=list(range(1, 13)),
    index=5
)

# Construim variabilele folosite de model
movie_age = 2026 - release_year
log_budget = np.log1p(budget)
log_vote_count = np.log1p(vote_count)
log_popularity = np.log1p(popularity)

input_data = pd.DataFrame({
    'movie_age': [movie_age],
    'log_budget': [log_budget],
    'budget': [budget],
    'release_year': [release_year],
    'vote_count': [vote_count],
    'vote_average': [vote_average],
    'log_popularity': [log_popularity],
    'log_vote_count': [log_vote_count]
})

input_data = input_data[features_app]

def interpret_prediction(di):
    if di < 1:
        return "🔴 Risc ridicat de flop — filmul este estimat să performeze sub așteptări."
    elif di < 3:
        return "🟡 Performanță apropiată de așteptări — filmul poate recupera investiția."
    else:
        return "🟢 Succes peste așteptări — filmul are potențial financiar ridicat."

st.markdown("---")

if st.button("Estimează performanța filmului"):
    prediction = model.predict(input_data)[0]

    st.subheader("Rezultat predicție")
    st.metric("Disappointment Index estimat", f"{prediction:.2f}")

    interpretation = interpret_prediction(prediction)
    st.write(interpretation)

    st.markdown("""
    **Cum interpretăm rezultatul?**

    Disappointment Index compară performanța estimată a filmului cu venitul așteptat în funcție de buget.
    O valoare sub 1 indică o performanță sub așteptări, iar o valoare peste 1 indică faptul că filmul poate depăși pragul estimat.
    """)
