
from fastapi import FastAPI
from routers import article_router
from core.logger import setup_logging

setup_logging()

app = FastAPI(title="AI Agent Backend - Groq Version")

app.include_router(article_router.router)
