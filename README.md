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

## Webhook Troubleshooting

To watch clear trigger + execution status logs:

```bash
docker compose logs -f backend n8n \
  | grep --line-buffered -Ei "Forwarding session|accepted by n8n webhook|webhook|trigger|execution|success|failed|error" \
  | grep --line-buffered -Evi "python task runner in internal mode|N8N_RUNNERS_ENABLED -> Remove this environment variable"
```

This helps you quickly see:
- which webhook/trigger was called
- backend session handoff to n8n
- whether execution finished with success or failed

If logs are still noisy, restart n8n after pulling latest config:

```bash
docker compose up -d n8n --force-recreate
```

Optional (faster filtering): install ripgrep and use `rg` instead of `grep`.

If you see this warning:

`Failed to start Python task runner in internal mode ... Python 3 is missing`

on `n8n 2.7.x`, this is expected in internal runner mode and does not block JS code-node workflows. Do not use `N8N_RUNNERS_ENABLED` (deprecated/ignored in this version).

To apply config changes cleanly:

```bash
docker compose up -d n8n --force-recreate
```

If you later need Python execution, run task runners in external mode per n8n docs.

If you see this in n8n logs:

`Received request for unknown webhook: The requested webhook "POST article-processor" is not registered.`

Use this checklist:

1. Confirm the workflow contains a `Webhook` node with path `article-processor` and method `POST`.
2. Ensure workflow is **Active** when using:
   - `http://localhost:5678/webhook/article-processor`
3. If workflow is not active and you are testing from editor, click **Listen for test event** and use:
   - `http://localhost:5678/webhook-test/article-processor`
4. If you already started Docker once, existing `n8n_data` may still contain an old inactive workflow.
   Activate the workflow in n8n UI, or re-import `n8n/workflow.json`.
5. Restart backend after changing `N8N_WEBHOOK_URL`.

If n8n logs show:

`Forbidden - perhaps check your credentials?`

Check:

1. In n8n, open **Executions** and confirm which node failed (usually `Google Sheets`).
2. Share the target Google Sheet with your service account email (for example: `ai-agent@...iam.gserviceaccount.com`) as **Editor**.
3. In Google Cloud, enable both **Google Sheets API** and **Google Drive API** for the same project as the service account key.
4. In the `Google Sheets` node, set a valid sheet tab name (for example `Sheet1`) and confirm `documentId` points to an existing sheet.
5. In n8n credentials, re-test and save the Google credential, then run the workflow again.

---

## Recommended Groq Model

llama-3.1-8b-instant

Fast and cost-effective for summarization & insights.

## Video Presentation

[AI Article Processing Agent Video Presentation](https://youtu.be/QbPVbDDxyVM)
