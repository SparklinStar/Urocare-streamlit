import requests

url = "https://api.cloudflare.com/client/v4/accounts/78f84e7a44c04581f6beb072d05136d1/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
headers = {
    "Authorization": "Bearer nrh7rmLsTp0PXwggnTZR2oyP_MZuULPKFhetPyDo",
    "Content-Type": "application/json",
}

data = {
    "prompt": "cyberpunk girl with a katana",
}

response = requests.post(url, headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open("output_image.png", "wb") as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}, {response.text}")
