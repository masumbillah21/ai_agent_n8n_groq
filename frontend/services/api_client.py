
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/process")

def send_article_request(email, article_url):
    payload = {
        "email": email,
        "article_url": article_url
    }

    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=20)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {
            "status": "error",
            "message": f"Backend request failed: {exc}"
        }
