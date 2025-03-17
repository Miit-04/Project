import os
from openai import OpenAI
import json

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "default_key")
openai = OpenAI(api_key=OPENAI_API_KEY)

def analyze_symptoms(symptoms, age, gender, severity, duration, notes):
    """
    Analyze patient symptoms using OpenAI's GPT-4o model
    """
    try:
        prompt = f"""
        Analyze the following patient symptoms and provide potential diagnoses:
        
        Patient Information:
        - Age: {age}
        - Gender: {gender}
        - Symptoms: {', '.join(symptoms)}
        - Severity (1-10): {severity}
        - Duration (days): {duration}
        - Additional Notes: {notes}
        
        Provide diagnosis in JSON format with the following structure:
        {{
            "confidence": float (0-1),
            "conditions": [
                {{
                    "name": string,
                    "confidence": float (0-100),
                    "description": string
                }}
            ]
        }}
        """
        
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a medical diagnosis assistant AI. Provide detailed medical analysis."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
        
    except Exception as e:
        print(f"Error in symptom analysis: {str(e)}")
        return None
