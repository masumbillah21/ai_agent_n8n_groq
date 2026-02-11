# AI Article Processing Agent

## Overview

This project is a mini AI workflow system built using:

- Streamlit → Frontend UI
- FastAPI (Async) → Backend API
- n8n → Workflow Automation Engine
- Groq API → AI Summarization & Insights
- Google Sheets API → Store Results
- Email (SMTP/Gmail) → Send Results to User

---

## System Architecture

```
Streamlit (Frontend)
        ↓
FastAPI Backend
        ↓
n8n Webhook
        ↓
Scrape Article
        ↓
Groq API (Summarize)
        ↓
Groq API (Insights)
        ↓
Google Sheets (Append Row)
        ↓
Email to User
```
---

## Required API Keys

## Groq API Key

Get your key from:
https://console.groq.com/keys

Add to .env:

GROQ_API_KEY=your_groq_api_key_here

---

## Google Sheets API (Service Account Setup)

Google Sheets does NOT use a simple API key for write access.

## Steps

1. Go to Google Cloud Console
2. Create a new project
3. Enable:
   - Google Sheets API
   - Google Drive API
4. Create Service Account
5. Generate JSON key
6. Share your Google Sheet with the service account email
7. Add credentials inside n8n

---

## Installation

You can run the system using either:

- Manual Setup  
- Docker Setup (Recommended)

---

## Manual Setup

## Backend Setup

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create .env:

N8N_WEBHOOK_URL=http://localhost:5678/webhook/article-processor

Run:

uvicorn main:app --reload

Backend runs on:
http://localhost:8000

---

## Frontend Setup

cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create .env:

BACKEND_URL=http://localhost:8000/process

Run:

streamlit run app.py

Frontend runs on:
http://localhost:8501

---

## Run n8n

Install:

npm install -g n8n

Start:

n8n

Open:
http://localhost:5678

Import workflow.json and activate it.

---

## Docker Setup (Recommended)

Install Docker Desktop.

Copy:

.env.example → .env

Then run:

docker-compose up --build

Services:

Frontend → http://localhost:8501  
Backend → http://localhost:8000  
n8n → http://localhost:5678  

---

## Extract Response

Use expression in n8n:

{{$json["choices"][0]["message"]["content"]}}

---

## Testing Flow

1. Open Streamlit UI
2. Enter email + article URL
3. Submit
4. Check:
   - Backend logs
   - n8n execution
   - Google Sheets updated
   - Email received

---

## Recommended Groq Model

llama-3.1-8b-instant

Fast and cost-effective for summarization & insights.
