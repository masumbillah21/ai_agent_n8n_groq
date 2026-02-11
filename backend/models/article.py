
from pydantic import BaseModel, EmailStr

class ArticleRequest(BaseModel):
    email: EmailStr
    article_url: str
