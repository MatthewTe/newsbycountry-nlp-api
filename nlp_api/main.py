from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import uvicorn

app = FastAPI()

class ArticleContent(BaseModel):
    id: int
    title: str
    raw_text: str | None

nlp = spacy.load("en_core_web_sm")

@app.post("/article/")
async def process_article_text(article_content: ArticleContent):

    # Performing named entity recogniton on the text body:
    doc = nlp(article_content.raw_text)

    GEPs = [{"label": entity.text, "label_type": entity.label_} for entity in doc.ents]

    return GEPs

