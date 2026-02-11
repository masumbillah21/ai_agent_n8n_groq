
from fastapi import APIRouter
from models.article import ArticleRequest
from services.n8n_service import forward_to_n8n
from services.session_service import generate_session_id
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/process")
async def process_article(data: ArticleRequest):
    session_id = generate_session_id()

    payload = {
        "email": data.email,
        "article_url": data.article_url,
        "session_id": session_id
    }

    logger.info(f"Forwarding session {session_id} to n8n")
    await forward_to_n8n(payload)

    return {"status": "sent", "session_id": session_id}
