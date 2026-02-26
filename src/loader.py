import json

def load_faq_text():
    with open("data/faq.txt", "r") as f:
        return f.read().lower()

def load_business_info():
    with open("data/business_info.json", "r") as f:
        return json.load(f)
    