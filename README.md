🧠 Personality Prediction App

This is a Streamlit web application that uses a trained LightGBM classifier to predict whether a person is an Introvert or Extrovert based on their social behavior and lifestyle features.

🚀 Features

    Predicts personality type using:

        Time spent alone

        Stage fear

        Social event attendance

        Going outside frequency

        Feeling drained after socializing

        Friend circle size

        Post frequency on social media

    Interactive Streamlit UI

    Built using a trained LightGBM model

    Fast, efficient, and easy to use

📁 Project Structure

├── data/                 # (optional) Raw or cleaned dataset
├── models/               # Saved model (.pkl file)
│   └── lgbm_model.pkl
├── streamlit_app.py      # Main Streamlit app
├── requirements.txt      # Required Python packages
└── README.md             # This file

⚙️ How to Run the App

    Clone the repository or download the project folder:

git clone <your-repo-url>
cd <project-folder>

Create a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

Install the required packages:

pip install -r requirements.txt

Run the Streamlit app:

    streamlit run streamlit_app.py

📦 Requirements

Add the following to your requirements.txt (already assumed):

streamlit
pandas
numpy
scikit-learn
lightgbm

📌 Notes

    Ensure that the file lgbm_model.pkl is present inside the models/ folder.

    The model expects a specific set of features with the same encoding used during training.

    Works locally or can be deployed to services like Streamlit Cloud or Heroku.

🧑‍💻 Author

Made with ❤️ by SanjayBista1010
