
# AI Doctor Brain – Medical Image Analysis using Vision LLM

AI Doctor Brain is a Streamlit-based web application that allows users to upload medical images (such as MRI or X-ray scans) and ask diagnostic questions. The system uses a multimodal large language model through the Groq API to analyze the image and generate responses.

This project demonstrates the integration of computer vision capabilities with large language models for medical image interpretation.

---

## Project Overview

The application enables users to:

- Upload a medical image (JPG, JPEG, PNG)
- Enter a diagnostic question related to the image
- Receive an AI-generated analysis based on both the image and the query

The system uses a multimodal LLM model hosted via the Groq API to process both text and image input.

---

## Features

- Medical image upload support
- Natural language question input
- Multimodal AI processing (text + image)
- Real-time AI-generated responses
- Secure API key input field
- Clean and simple Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- Groq API
- LLaMA Vision Model
- Base64 encoding for image handling

---

## Model Used

Model:
meta-llama/llama-4-scout-17b-16e-instruct

The model processes both text prompts and image data to generate contextual responses.

---

## Project Structure
