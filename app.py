import streamlit as st
import pandas as pd
import joblib

# Load the saved brain
model = joblib.load('fake_profile_model.pkl')

st.title("Fake Profile Detection System")
st.write("Upload a CSV file containing suspect social media accounts. The system will classify them automatically.")

# Create a file uploader on the web interface
uploaded_file = st.file_uploader("Upload Profile Data (CSV)", type="csv")

if uploaded_file is not None:
    # Read the uploaded file
    input_data = pd.read_csv(uploaded_file)
    
    st.write("### Raw Data Preview")
    st.dataframe(input_data.head())

    # We only want to feed the exact columns the model was trained on
    features = ['profile_pic', 'nums_length_username', 'fullname_words', 'network_ratio']
    
    try:
        X_scan = input_data[features]
        
        if st.button("Run Security Scan"):
            st.write("Scanning profiles...")
            
            # The model predicts 0 (Genuine) or 1 (Fake)
            predictions = model.predict(X_scan)
            
            # The model also tells us how confident it is
            probabilities = model.predict_proba(X_scan)

            # Add the results back to the spreadsheet for the user to see
            input_data['Classification'] = ['FAKE' if pred == 1 else 'GENUINE' for pred in predictions]
            input_data['Confidence Score'] = [f"{prob[1]*100:.2f}%" if pred == 1 else f"{prob[0]*100:.2f}%" for pred, prob in zip(predictions, probabilities)]

            st.write("### Scan Results")
            # Highlight the fake accounts in red so they stand out
            def highlight_fakes(val):
                color = 'red' if val == 'FAKE' else 'green'
                return f'color: {color}'
            
            st.dataframe(input_data.style.map(highlight_fakes, subset=['Classification']))
            
    except KeyError:
        st.error("Error: The uploaded CSV is missing required columns. Ensure it has: profile_pic, nums_length_username, fullname_words, network_ratio.")