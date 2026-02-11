
import httpx
import os
import logging

logger = logging.getLogger(__name__)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

async def forward_to_n8n(payload):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(N8N_WEBHOOK_URL, json=payload)
            logger.info(f"n8n response: {response.status_code}")
        except Exception as e:
            logger.error(f"Error forwarding to n8n: {str(e)}")
