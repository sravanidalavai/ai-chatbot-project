Gym FAQ Chatbot (RAG + Tools)

This project is a simple Gym chatbot built using Python.

Features:
- Answers FAQ questions from faq.txt
- Uses business_info.json for structured data (hours, pricing, phone, address)
- Simple router decides whether to retrieve or use tool
- FastAPI wrapper for API usage

How to run:

pip install -r requirements.txt
uvicorn main:app --reload

Then open:
http://127.0.0.1:8000/docs