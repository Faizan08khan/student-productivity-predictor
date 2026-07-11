📊 Student Productivity Predictor

🚀 An interactive machine learning app that predicts student productivity based on lifestyle, study habits, and academic performance.

📖 Project Overview:

This project applies machine learning to education by predicting a student’s productivity score. The dataset includes factors such as study hours, sleep, attendance, GPA, stress, motivation, and more.

The app uses a Random Forest Regressor trained on this dataset. Predictions are made through a Streamlit interface, where users can input details for one student and instantly see the estimated productivity score.

This project demonstrates the complete workflow:

Data preprocessing (handling missing values, encoding categorical variables).

Feature scaling (using StandardScaler to normalize inputs).

Model training (Random Forest Regressor).

Deployment (Streamlit app with interactive UI).

🛠 Tech Stack:

🐍 Python

🎛️ Streamlit for interactive UI

📊 pandas for data handling

🤖 scikit‑learn for ML model training

✨ Features:

🎛️ Interactive form with sliders and dropdowns for student details.

⚡ Real‑time productivity score prediction.

🧹 Automatic preprocessing: missing values handled, categorical variables encoded.

📂 Single‑file workflow (app.py) — train + predict in one place.

🌐 Easy deployment on Streamlit Cloud.

📈 Use Case:

This app helps visualize how different factors influence student productivity.

Students can self‑assess their habits 📚

Educators can explore performance drivers 🎓

Data science learners can study a practical ML deployment example 💡

🚀 Getting Started
Clone the repo and run locally:

bash
git clone https://github.com/your-username/student-productivity-predictor.git
cd student-productivity-predictor
pip install -r requirements.txt
streamlit run app.py
Then open http://localhost:8501 in your browser to interact with the app.

🔗 Links:

🌐 Live Demo: [Streamlit app link]

💻 Code & Dataset: [GitHub repo link]

📒 Notebook Version: [Colab link]
