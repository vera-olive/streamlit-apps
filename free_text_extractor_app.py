import os
import streamlit as st
import json
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage

st.title("Free Text Clinical Data Extractor")

api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key to proceed.")
    st.stop()   

st.markdown(
    """
    <p style="font-size:15px;">
    This is a <b>Streamlit app</b> that extracts structured medical information from a 
    <b>free-text doctor's note</b> using <b>LangChain</b> and <b>OpenAI's GPT-4</b>.
    </p>
    """,
    unsafe_allow_html=True,
)

doctor_note = st.text_area("Enter the doctor's note:", "")

if st.button("Extract Information"):
    if not doctor_note.strip():
        st.warning("Please enter a doctor's note before extracting information.")
    else:
        llm = ChatOpenAI(model_name="gpt-4", temperature=0, api_key=api_key)

        prompt = f"""
        Extract and structure the following information from the free-text doctor's note:
        - Patient details (age, gender)
        - Symptoms (Only the name of the symptom, without duration, frequency, or severity)
        - Suspected Diagnoses
        - Recommended Lab Tests
        - Prescriptions
        - Follow-up Appointments

        Return the data in **valid JSON format**.

        If the text contains **no medical information**, respond with:
        {{
            "message": "No clinical information detected"
        }}

        Doctor's Note:
        {doctor_note}
        """

        response = llm([SystemMessage(content=prompt)])
        response_text = response.content.strip()

        try:
            structured_data = json.loads(response_text)

            if "message" in structured_data and structured_data["message"] == "No clinical information detected":
                st.warning("No clinical information detected.")
            else:
                st.subheader("Extracted Information")
                st.json(structured_data)

        except json.JSONDecodeError:
            st.error("The AI did not return a valid JSON response. Try using a more medical-focused note.")
            st.text("Raw Response from AI:")
            st.write(response_text) 
