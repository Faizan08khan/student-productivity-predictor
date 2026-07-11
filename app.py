import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

st.title("📊 Student Productivity Predictor")

# --- Load and train model once ---
# Replace with your actual dataset file
df = pd.read_csv("Student_Productivity_Dataset.csv")

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=['Gender','Internet_Quality','Part_Time_Job','Performance_Category'], drop_first=True)

# Features and target
X = df.drop(['Productivity_Score','Student_ID'], axis=1)
y = df['Productivity_Score']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

expected_columns = list(X.columns)

# --- Input form for one student ---
st.markdown("Provide the following details to estimate productivity score:")

age = st.slider("Age", 15, 30, 20)
study_hours = st.slider("Study Hours Per Day", 0, 12, 4)
sleep_hours = st.slider("Sleep Hours Per Night", 0, 12, 7)
screen_time = st.slider("Screen Time (hours/day)", 0, 12, 5)
social_media = st.slider("Social Media Hours", 0, 12, 3)
attendance = st.slider("Attendance Percentage", 0, 100, 85)
assignments = st.number_input("Assignments Completed", 0, 100, 10)
class_participation = st.slider("Class Participation Score", 0, 100, 70)
physical_activity = st.slider("Physical Activity Hours/Week", 0, 20, 3)
stress_level = st.slider("Stress Level (1–10)", 1, 10, 5)
motivation_level = st.slider("Motivation Level (1–10)", 1, 10, 7)
ai_tool_usage = st.slider("AI Tool Usage Hours/Week", 0, 40, 5)
previous_gpa = st.slider("Previous Semester GPA", 0.0, 10.0, 7.0)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
internet_quality = st.selectbox("Internet Quality", ["Good", "Poor"])
part_time_job = st.selectbox("Part-Time Job", ["Yes", "No"])

# --- Predict button ---
if st.button("Predict Productivity"):
    raw_input = {
        "Age": age,
        "Study_Hours_Per_Day": study_hours,
        "Sleep_Hours_Per_Night": sleep_hours,
        "Screen_Time_Hours": screen_time,
        "Social_Media_Hours": social_media,
        "Attendance_Percentage": attendance,
        "Assignments_Completed": assignments,
        "Class_Participation_Score": class_participation,
        "Physical_Activity_Hours_Per_Week": physical_activity,
        "Stress_Level": stress_level,
        "Motivation_Level": motivation_level,
        "AI_Tool_Usage_Hours_Per_Week": ai_tool_usage,
        "Previous_Semester_GPA": previous_gpa,
        "Gender_" + gender: 1,
        "Internet_Quality_" + internet_quality: 1,
        "Part_Time_Job_" + part_time_job: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Fill missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]
    st.success(f"📈 Predicted Productivity Score: {prediction:.2f}")
