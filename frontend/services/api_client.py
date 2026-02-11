
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/process")

def send_article_request(email, article_url):
    payload = {
        "email": email,
        "article_url": article_url
    }

    response = requests.post(BACKEND_URL, json=payload)
    return response.json()
