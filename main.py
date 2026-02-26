from fastapi import FastAPI
from src.loader import load_faq_text, load_business_info
from src.bot import answer_question
from src.schemas import ChatRequest, ChatResponse

app = FastAPI(title="Gym FAQ Chatbot")

faq_text = load_faq_text()
business_data = load_business_info()

@app.get("/")
def home():
    return {"message": "Gym bot is running. Go to /docs"}

@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    ans = answer_question(payload.question, faq_text, business_data)
    return ChatResponse(answer=ans)