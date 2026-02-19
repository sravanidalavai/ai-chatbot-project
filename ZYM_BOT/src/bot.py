def answer_question(question, faq_text, bussiness_data):
    question = question.lower()

    if "price" in question:
        return f"Our pricing is: {bussiness_data['pricing']}"

    if "address" in question or "location" in question:
        return f"We are located at: {bussiness_data['address']}"

    if "hours" in question:
        return f"Our hours: {bussiness_data['hours']}"

    if "phone" in question:
        return f"Call us at: {bussiness_data['phone']}"

    if question in faq_text:
        return "This question is covered in FAQ."

    return "Sorry, I don't know. Please contact gym."