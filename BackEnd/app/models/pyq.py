from datetime import datetime

def pyq_model(pyq: dict):
    return {
        "subject": pyq["subject"],
        "year": pyq["year"],
        "question": pyq["question"],
        "answer": pyq.get("answer"),
        "topic": pyq.get("topic"),
        "created_at": datetime.utcnow()
    }
