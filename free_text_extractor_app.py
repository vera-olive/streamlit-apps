import os
import streamlit as st
import json
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("OpenAI API key not found. Please set it as an environment variable before running the app.")
    st.stop() 

llm = ChatOpenAI(model_name="gpt-4", temperature=0.1, api_key=openai_api_key)

st.title("Free text clinical data extractor")

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
    if doctor_note.strip(): 

        prompt = f"""
        Extract and structure the following information from the free-text doctor's note:
        - Patient age
        - Patient gender
        - Symptoms ((Only the name of the symptom, without duration, frequency, or severity)
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
    else:
        st.warning("Please enter a doctor's note before extracting information.")

