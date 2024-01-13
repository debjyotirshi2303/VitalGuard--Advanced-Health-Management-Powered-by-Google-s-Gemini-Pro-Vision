from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()

# Configure Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to use Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to handle uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Setup
st.set_page_config(page_title="VitalGuard: Advanced Health Management Powered by Google's Gemini Pro-Vision", menu_items={'About': "created by Debjyotirshi Majumder"})
st.header("VitalGuard: Advanced Health Management Powered by Google's Gemini Pro-Vision")

# Sidebar for additional options
with st.sidebar:
    st.info("Configure Settings")
    resize_option = st.checkbox("Enable Image Resizing")

# User inputs
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
user_age = st.number_input("Enter your age:", min_value=1, max_value=120, key="age")
image = ""

# Display uploaded image with resizing option
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    if resize_option:
        size = st.slider("Resize Image", 100, 1000, 500)
        st.image(image, caption="Uploaded Image.", width=size)
    else:
        st.image(image, caption="Uploaded Image.", use_column_width=True)

# Define input prompt for Gemini API with f-string
input_prompt = f"""
You are an expert nutritionist required to analyze food items in an image and calculate the total calories. 
Provide details of every food item with calorie intake in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
---
Total calories:

Recommendation based on user's age ({user_age} years): (By how much should the user increase or decrease the calorie intake)
"""

# Handle submit action
submit = st.button("Tell me the total calories")
if submit:
    with st.spinner('Processing...'):
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_text, image_data, input_prompt)
            time.sleep(2)  # Simulate processing time
            st.subheader("Response: ")
            st.info(response)  # Display response in an info box
        except FileNotFoundError:
            st.error("Please upload an image to proceed.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
