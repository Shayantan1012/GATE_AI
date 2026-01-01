from datetime import datetime

def activity_log_model(log: dict):
    return {
        "admin_id": log["admin_id"],
        "action": log["action"],
        "target": log.get("target"),
        "timestamp": datetime.utcnow()
    }
