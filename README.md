# 🫀 Heart Disease Prediction Web Application

This project is a web-based machine learning application for predicting the risk of heart disease. It leverages a **Random Forest model**, integrates **Large Language Models (LLMs)** for explanations, and is deployed via **Docker** for portability.

---

## 📌 Features

- Predict heart disease risk using clinical features
- Interactive web interface (Python + HTML)
- Explanations generated using LLMs (via API)
- Synthetic data generation (GPT-2)
- Containerized using Docker for easy deployment

---

## 🧠 Technologies Used

- Python (Flask + Waitress)
- HTML/CSS (for frontend)
- Scikit-learn (Random Forest)
- Pandas & NumPy (data handling)
- Hugging Face Transformers (GPT-2)
- Google Generative Language API (for LLM explanations)
- Docker

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Load Docker image from `.tar`
Download the Docker image from the link below and load it:

🔗 **[Download heart-app.tar from Google Drive](https://drive.google.com/drive/u/3/my-drive)**

```bash
docker load -i heart-app.tar
```

### 3. Run the Docker container
```bash
docker run -p 5000:5000 heart-disease-prediction:latest
```

Access the app in your browser: [http://localhost:5000](http://localhost:5000)

---

## ⚙️ LLM Integration

The app uses an LLM (like Google PaLM/Gemini) to explain model predictions. Ensure internet access is available inside your Docker container.

**If using Google Generative Language API**, you’ll need:
- API Key
- Internet access
- Proper DNS resolution (consider `--dns=8.8.8.8` if needed)

---

## ⚠️ Known Issues

- **FutureWarning with `pd.read_json`**:
  Fix by wrapping with `StringIO`:
  ```python
  from io import StringIO
  pd.read_json(StringIO(data))
  ```

- **LLM Explanation Timeout / DNS Error**:
  Ensure Docker has outbound internet and DNS access:
  ```bash
  docker run --dns=8.8.8.8 -p 5000:5000 heart-disease-prediction:latest
  ```

---

## 📊 Dataset

Used the UCI Heart Disease dataset (`heart.csv`) with features such as:
- Age, Sex, Blood Pressure, Cholesterol, etc.

Also includes synthetic records generated via GPT-2 (`generate_synthetic_data.py`).

---

## 🧪 Model

Trained a **Random Forest Classifier** and saved using `joblib`:
- Model file: `random_forest_model.pkl`
- Loaded at runtime inside the app

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](screenshots/home_page.png)

### 📊 Prediction Result
![Prediction Result](screenshots/prediction_result.png)

### 💬 LLM Explanation
![LLM Explanation](screenshots/llm_explanation.png)


## 📁 Project Structure

```
├── app.py                   # Main application
├── templates/               # HTML templates
├── static/                  # CSS/JS assets
├── heart.csv                # Dataset
├── generate_synthetic_data.py
├── random_forest_model.pkl  # Trained model
├── Dockerfile
├── heart-app.tar            # Docker image (optional)
└── README.md
```

---

## 📬 Contact

Developed by **N. Abhiram Chowdary**  
B.Tech CSE (AI & ML), SRM Institute of Science & Technology  
📧 [abhiramchowdary86@gmail.com]

---

