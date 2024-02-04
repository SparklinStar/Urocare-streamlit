# Imports
import os
import streamlit as st
from apikey import apikey
import requests

# CSS styling
css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 85%;
  padding: 0 1.25rem;
  color: #fff;
}
'''
st.write(css, unsafe_allow_html=True)

from PIL import Image  # You need to install the Pillow library for image handling
import requests

url = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
headers = {
    "Authorization": "Bearer nrh7rmLsTp0PXwggnTZR2oyP_MZuULPKFhetPyDo",
    "Content-Type": "application/json",
}

data = {
    "prompt": "doctor avatar with a stethoscope, and a white coat, white background, minimalistic",
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    with open("output_image.png", "wb") as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}, {response.text}")
col1, col2 = st.columns(2)
# Load the image from a file or any source
with col1:
    image_path = "output_image.png"  # Replace with the path to your image file
    image = Image.open(image_path)

    # Display the image in the Streamlit app
   
    # Title and Description
    st.title("UroCare")
    st.write("Your friendly Urologist Doctor. Ask me any question related to sex health and I will provide you with the best possible answer. I am here to help you.")

with col2:
    st.image(image,  width=50, use_column_width=False)
    # User input
    input_text = st.text_input('Enter message ')

    API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/"
    headers = {"Authorization": "Bearer SwP60DGlLcaOHiPHV3fhgUUZ0huUeKAXlbHoQthQ"}

    def run(model, inputs):
        input = { "messages": inputs }
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
        return response.json()

    inputs = [
        { "role": "system", "content": "You are a Urologist Doctor with the name Dr. Pal who provides friendly assistance and helps to diagnose patients. Dont say you are an ai. Strictly Provide answers only if the question is in the field of Urology " },
        { "role": "user", "content": input_text}
    ];
    output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    print(output)

    if st.button('Send Message') and input_text:
        with st.spinner('Generating response...'):
            try:
                # Generate satirical response
                response = output
                st.write(response['result']['response'])
                # Store conversation
                st.session_state.past.append(input_text)
                st.session_state.generated.append(response)

                #Display conversation in reverse order
            

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
