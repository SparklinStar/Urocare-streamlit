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

# url = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {
#     "Authorization": "Bearer nrh7rmLsTp0PXwggnTZR2oyP_MZuULPKFhetPyDo",
#     "Content-Type": "application/json",
# }

# data = {
#     "prompt": "doctor avatar with a stethoscope, and a white coat, white background, minimalistic",
# }


# response = requests.post(url, headers=headers, json=data)
# if response.status_code == 200:
#     with open("doctor.png", "wb") as f:
#         f.write(response.content)
# else:
#     print(f"Error: {response.status_code}, {response.text}")

# # Load the image from a file or any source

  

# url = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {
#     "Authorization": "Bearer nrh7rmLsTp0PXwggnTZR2oyP_MZuULPKFhetPyDo",
#     "Content-Type": "application/json",
# }

# data = {
#     "prompt": "user avatar with a face, white background, minimalistic",
# }


# response = requests.post(url, headers=headers, json=data)
# if response.status_code == 200:
#     with open("user.png", "wb") as f:
#         f.write(response.content)
# else:
#     print(f"Error: {response.status_code}, {response.text}")

# Load the image from a file or any source



    # Display the image in the Streamlit app
   
    # Title and Description
st.title("UroCare")
st.write("Your friendly Urologist Doctor. Ask me any question related to urological health and I will provide you with the best possible answer. I am here to help you.")


    
   



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user",avatar="user.png").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/"
    headers = {"Authorization": "Bearer SwP60DGlLcaOHiPHV3fhgUUZ0huUeKAXlbHoQthQ"}

    def run(model, inputs):
        input = { "messages": inputs }
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
        return response.json()

    inputs = [
        { "role": "system", "content": "You are a Urologist Doctor with the name Dr. Pal who provides friendly assistance and helps to diagnose patients. Dont say you are an ai. Strictly Provide answers only if the question is in the field of Urology. Keep it short and simple easy to understand to the patient. " },
        { "role": "user", "content": prompt}
    ];
    response = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    print(response)
    
    
    # Display assistant response in chat message container
    with st.chat_message("assistant",avatar="doctor.png"):
        st.markdown(response['result']['response'])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response['result']['response']})
    

    

    
