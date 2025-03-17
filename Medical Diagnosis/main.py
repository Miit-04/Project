import streamlit as st
import plotly.graph_objects as go
from utils.ai_analysis import analyze_symptoms
from utils.medical_db import get_condition_info, COMMON_SYMPTOMS
import os

# Page configuration
st.set_page_config(
    page_title="Medical Diagnosis Assistant",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
with open('assets/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Sidebar
    st.sidebar.image("https://images.unsplash.com/photo-1516841273335-e39b37888115", use_container_width=True)
    st.sidebar.title("Medical Diagnosis Assistant")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Patient Symptom Analysis")

        # Patient Information
        with st.expander("Patient Information", expanded=True):
            age = st.number_input("Age", 0, 120, 25)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        # Symptom Selection
        with st.expander("Symptom Selection", expanded=True):
            selected_symptoms = st.multiselect(
                "Select Symptoms",
                options=COMMON_SYMPTOMS,
                help="Select all applicable symptoms"
            )

            severity = st.slider(
                "Symptom Severity",
                1, 10, 5,
                help="Rate the overall severity of symptoms"
            )

            duration = st.number_input(
                "Duration (days)",
                min_value=1,
                max_value=365,
                value=1,
                help="How long have you been experiencing these symptoms?"
            )

        # Additional Notes
        notes = st.text_area(
            "Additional Notes",
            help="Enter any additional relevant information"
        )

        if st.button("Analyze Symptoms", type="primary"):
            if len(selected_symptoms) < 1:
                st.error("Please select at least one symptom.")
                return

            with st.spinner("Analyzing symptoms..."):
                analysis_result = analyze_symptoms(
                    symptoms=selected_symptoms,
                    age=age,
                    gender=gender,
                    severity=severity,
                    duration=duration,
                    notes=notes
                )

                if analysis_result:
                    with col2:
                        st.header("Analysis Results")

                        # Display confidence gauge
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=analysis_result["confidence"] * 100,
                            domain={'x': [0, 1], 'y': [0, 1]},
                            gauge={
                                'axis': {'range': [0, 100]},
                                'bar': {'color': "#28A745"},
                                'threshold': {
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,
                                    'value': 70
                                }
                            }
                        ))
                        st.plotly_chart(fig)

                        # Display potential conditions
                        st.subheader("Potential Conditions")
                        for condition in analysis_result["conditions"]:
                            with st.container():
                                st.markdown(f"""
                                    <div class="condition-card">
                                        <h3>{condition['name']}</h3>
                                        <p>Confidence: {condition['confidence']}%</p>
                                        <p>{condition['description']}</p>
                                    </div>
                                """, unsafe_allow_html=True)

                                # Get additional condition information
                                condition_info = get_condition_info(condition['name'])
                                if condition_info:
                                    st.markdown("### Common Treatments")
                                    st.write(condition_info['treatments'])

                                    st.markdown("### Recommended Actions")
                                    st.write(condition_info['recommendations'])

                else:
                    st.error("An error occurred during analysis. Please try again.")

if __name__ == "__main__":
    main()