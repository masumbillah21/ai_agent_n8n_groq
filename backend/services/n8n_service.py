
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
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            body = e.response.text[:500]
            logger.error(
                "n8n request failed with status %s for URL %s: %s",
                status_code,
                N8N_WEBHOOK_URL,
                body,
            )
            raise
        except Exception as e:
            logger.error(f"Error forwarding to n8n: {str(e)}")
            raise
