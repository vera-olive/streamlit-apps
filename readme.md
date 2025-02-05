# Clinical Data Extractor

This is a **Streamlit app** that extracts structured medical information from a **free-text doctor's note** using **LangChain** and **OpenAI's GPT-4**.

- Users can input a **doctor's note** via a text box.
- The app extracts clinical details, if available:
  - Patient details
  - Symptoms
  - Suspected diagnoses
  - Recommended lab tests
  - Prescriptions
  - Follow-up appointments
- Output is displayed in **JSON format**.

## Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/your-repo.git
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Have an OpenAI API key

This app requires an **OpenAI API key**. You can set it as an **environment variable** if running locally or enter it directly in the app.

```bash
export OPENAI_API_KEY="your-api-key"
```

### 4️⃣ Run the App
```bash
streamlit run free_text_extractor_app.py
```


---

🚀🚀🚀 
