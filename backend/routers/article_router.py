
from fastapi import APIRouter
from fastapi import HTTPException
import httpx
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
    try:
        await forward_to_n8n(payload)
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"n8n returned {e.response.status_code}. Verify webhook path and workflow activation.",
        ) from e
    except Exception as e:
        raise HTTPException(status_code=502, detail="Failed to reach n8n webhook") from e

    return {"status": "sent", "session_id": session_id}
