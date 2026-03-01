
import streamlit as st
import base64
from groq import Groq

st.set_page_config(page_title="🧠 AI Doctor Brain", layout="centered")
st.title("🧠 AI Doctor Brain")
st.write("Upload a medical image and ask a diagnostic question.")

# Step 1: Input API Key
GROQ_API_KEY = st.text_input("Enter your GROQ API Key:", type="password")

# Step 2: Upload image and enter query
uploaded_image = st.file_uploader("Upload an image (e.g., MRI, X-ray, etc.)", type=["jpg", "jpeg", "png"])
query = st.text_area("Ask your question:")

# Step 3: Analyze
if st.button("Analyze") and uploaded_image and query and GROQ_API_KEY:
    image_bytes = uploaded_image.read()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    client = Groq(api_key=GROQ_API_KEY)
    model = "meta-llama/llama-4-scout-17b-16e-instruct"

    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": query},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
        ]
    }]

    with st.spinner("Analyzing..."):
        try:
            response = client.chat.completions.create(messages=messages, model=model)
            st.success("Diagnosis Response:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Error: {e}")
