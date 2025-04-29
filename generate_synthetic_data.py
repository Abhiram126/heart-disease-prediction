import pandas as pd
from transformers import pipeline

# Load GPT model for data generation
generator = pipeline("text-generation", model="gpt2")

# Generate synthetic patient data
def generate_patient():
    prompt = "Generate a synthetic heart disease patient record with age, sex, cholesterol, blood_pressure."
    generated_text = generator(prompt, max_length=50, do_sample=True)[0]["generated_text"]
    return generated_text

# Generate 5 synthetic records
synthetic_data = [generate_patient() for _ in range(5)]
print(synthetic_data)
