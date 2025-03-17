# Mock medical database with common symptoms and conditions
COMMON_SYMPTOMS = [
    "Fever",
    "Headache",
    "Fatigue",
    "Cough",
    "Shortness of breath",
    "Chest pain",
    "Abdominal pain",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Joint pain",
    "Muscle aches",
    "Sore throat",
    "Runny nose",
    "Loss of taste/smell",
    "Dizziness",
    "Skin rash",
    "Back pain",
    "Anxiety",
    "Depression"
]

CONDITIONS_DB = {
    "Common Cold": {
        "treatments": [
            "Rest",
            "Hydration",
            "Over-the-counter medications"
        ],
        "recommendations": [
            "Monitor symptoms",
            "Seek medical attention if symptoms worsen",
            "Practice good hygiene"
        ]
    },
    "Influenza": {
        "treatments": [
            "Antiviral medications",
            "Rest",
            "Hydration"
        ],
        "recommendations": [
            "Isolate to prevent spread",
            "Monitor temperature",
            "Seek immediate care if breathing difficulties occur"
        ]
    },
    # Add more conditions as needed
}

def get_condition_info(condition_name):
    """
    Retrieve information about a specific medical condition
    """
    return CONDITIONS_DB.get(condition_name, None)
