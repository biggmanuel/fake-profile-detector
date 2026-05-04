# 🛡️ Fake Profile Detection System

## Overview
Social networking platforms are increasingly saturated with automated botnets and fabricated identities. This project provides an automated, intelligent countermeasure. 

This repository contains a **Fake Profile Detection System** powered by a Random Forest machine learning algorithm. Instead of relying on subjective human moderation, the system extracts and analyzes structural behavioral biometrics—such as follower-to-following network ratios, username digit density, and profile completion metrics—to identify the underlying mathematical signatures of automated accounts in milliseconds.

## ✨ Features
* **Machine Learning Engine:** Utilizes a trained Random Forest Classifier for high accuracy and resistance to data noise.
* **Batch Processing:** Ingests raw profile parameters via CSV upload for rapid, large-scale scanning.
* **Interactive Dashboard:** Deployed using Streamlit, providing a clean UI for administrators to run scans without writing code.
* **Confidence Scoring:** Outputs not just a binary classification (GENUINE/FAKE), but a mathematical probability score for every analyzed profile.
* **Visual Output:** Automatically color-codes results (Red for bots, Green for humans) for immediate triage.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Machine Learning:** `scikit-learn`
* **Data Manipulation:** `pandas`, `numpy`
* **Frontend/UI:** `streamlit`
* **Model Serialization:** `joblib`

## 🚀 Local Installation & Setup
To run this prototype on your local machine, ensure you have Python 3.10+ installed, then follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/fake-profile-detector.git](https://github.com/yourusername/fake-profile-detector.git)
cd fake-profile-detector

2. Install required dependencies:
pip install -r requirements.txt

3. (Optional) Retrain the Model:
If you want to train the model from scratch using the provided dataset, run the backend engine:
python model_builder.py

4. Launch the Dashboard:
Start the Streamlit server to open the graphical user interface in your browser:
python -m streamlit run app.py

📊 Dataset Structure
The system is designed to ingest standard CSV files containing social media metadata. The required input columns are:
profile_pic: Binary (1 if present, 0 if missing)
nums_length_username: Float (Ratio of numbers to letters in the username)
fullname_words: Integer (Word count of the display name)
network_ratio: Float (Follower-to-following ratio)
A sample payload (social_data_final.csv) is included in this repository for testing purposes.

🎓 Academic Disclaimer
This project was developed as a B.Sc. Computer Science research prototype. It is designed as a proof-of-concept for detecting automated accounts using tabular heuristic data and is not currently connected to live social media APIs.
