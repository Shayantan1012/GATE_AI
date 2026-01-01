from datetime import datetime

def document_model(doc: dict):
    return {
        "user_id": doc["user_id"],
        "filename": doc["filename"],
        "file_path": doc["file_path"],
        "content_type": doc["content_type"],
        "created_at": datetime.utcnow()
    }
