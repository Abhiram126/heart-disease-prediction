from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import joblib
import pandas as pd
import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API Key not found. Please set it in your .env file.")

# Configure Gemini AI
print("Environment Variables:", os.environ)

genai.configure(api_key=api_key)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load trained Random Forest model
logging.info("Loading Random Forest model...")
model = joblib.load("random_forest_model.pkl")
logging.info("Random Forest model loaded successfully.")

def generate_explanation(prediction, input_data):
    try:
        chat_model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        The patient has {'low' if prediction == 1 else 'high'} risk of heart disease based on the following data:

        {input_data.to_string(index=False)}

        Provide a detailed explanation considering:
        1. The most influential factors leading to this prediction.
        2. How specific features (age, cholesterol, blood pressure, etc.) impacted the outcome.
        3. Patterns or correlations identified by the model.
        4. A clear and simple explanation that a non-medical professional can understand.
        """
        response = chat_model.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error generating explanation: {e}")
        return str(e)

@app.route("/")
def first_page():
    logging.info("Rendering first page.")
    return render_template("firstpage.html")

@app.route("/index", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            logging.info("Processing form input data.")
            input_data = pd.DataFrame([{key: float(value) for key, value in request.form.items()}])
            
            session["data"] = input_data.to_json()
            logging.info("Data successfully processed and stored in session.")
            return redirect(url_for('predict'))
        except Exception as e:
            logging.error(f"Error processing input data: {e}")
            return render_template("prediction.html", error=str(e))
    return render_template("index.html", result=None)

@app.route("/predict")
def predict():
    logging.info("working")
    try:
        data = session.get('data')
        if not data:
            raise ValueError("No data found. Please submit the form first.")
        
        input_data = pd.read_json(data)
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0].tolist()

        explanation = generate_explanation(prediction, input_data)

        response = {
            "prediction": int(prediction),
            "probability": probability,
            "explanation": explanation
        }
        return render_template("prediction.html", result=response)
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    from waitress import serve
    logging.info("Starting application using Waitress on port 5000.")
    print("Application is running. Access it at: http://localhost:5000")
    serve(app, host='0.0.0.0', port=5000) 
