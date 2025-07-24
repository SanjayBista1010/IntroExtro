import streamlit as st
import joblib
import pandas as pd

model = joblib.load('models/lgbm_model.pkl')

yes_no_map = {'No': 0, 'Yes': 1}

st.title("Personality Prediction")

time_alone = st.number_input("Time Spent Alone", min_value=0.0, max_value=12.0, step=0.1)
stage_fear = st.selectbox("Stage Fear", options=["No", "Yes"])
social_event = st.slider("Social Event Attendance", 0, 10)
going_outside = st.slider("Going Outside Frequency", 0, 7)
drained_after = st.selectbox("Drained After Socializing", options=["No", "Yes"])
friends_circle = st.slider("Friends Circle Size", 0, 15)
post_freq = st.slider("Post Frequency", 0, 10)

input_df = pd.DataFrame([[
    time_alone,
    yes_no_map[stage_fear],
    social_event,
    going_outside,
    yes_no_map[drained_after],
    friends_circle,
    post_freq
]], columns=[
    'Time_spent_Alone',
    'Stage_fear',
    'Social_event_attendance',
    'Going_outside',
    'Drained_after_socializing',
    'Friends_circle_size',
    'Post_frequency'
])

if st.button("Predict Personality"):
    st.write("Input data:", input_df)
    pred = model.predict(input_df)[0]
    st.write("Raw prediction:", pred)
    label = "Extrovert" if pred == 1 else "Introvert"
    st.success(f"Predicted Personality: {label}")
